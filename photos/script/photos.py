#!/usr/bin/env python3
import os
import shutil
from PIL import Image
import datetime
import hashlib
import configparser
import logging
from logging.handlers import RotatingFileHandler
import exifread
import pyheif
import sqlite3

# 定义常量
EXIF_DATE_TIME_ORIGINAL = 36867
ROOT_PATH = '/photos'
CONFIG_PATH = os.path.join(ROOT_PATH, 'config')
LOGS_PATH = os.path.join(ROOT_PATH, 'logs')
DB_FOLDER = os.path.join(CONFIG_PATH, 'db')

# 从ini文件中读取配置信息，将ini文件的路径改为/photos/config/settings.ini，并加上了os.path.join函数
config = configparser.ConfigParser()
config.read(os.path.join('/photos', 'config', 'settings.ini'))
photo_formats = config.get('formats', 'photo_formats').split(',')
video_formats = config.get('formats', 'video_formats').split(',')
low_res_folder_name = config.get('folders', 'low_res_folder_name')
small_size_folder_name = config.get('folders', 'small_size_folder_name')
duplicated_folder_name = config.get('folders', 'duplicated_folder_name')
screenshot_folder_name = config.get('folders', 'screenshot_folder_name')
small_size_threshold = config.getint('thresholds', 'small_size_threshold')
low_res_width_threshold = config.getint('thresholds', 'low_res_width_threshold')
low_res_height_threshold = config.getint('thresholds', 'low_res_height_threshold')
Image.MAX_IMAGE_PIXELS = config.getint('thresholds', 'MAX_IMAGE_PIXELS')

# 定义源文件夹地址、输出文件夹地址
source_paths_name = config.get('paths', 'source_paths').split(',')
source_paths_prefix = os.path.join(ROOT_PATH, 'data')
source_paths = [os.path.join(source_paths_prefix, path) for path in source_paths_name]
target_paths_name = config.get('paths', 'target_paths').split(',')
target_paths_prefix = os.path.join(ROOT_PATH, 'data')
target_paths = [os.path.join(target_paths_prefix, path) for path in target_paths_name]

# 日志变量-字典
log_dict = {
    'log_photos_low_res': os.path.join(LOGS_PATH, *source_paths_name, 'move', 'low_res.log'),
    'log_photos_small_size': os.path.join(LOGS_PATH, *source_paths_name, 'move', 'small_size.log'),
    'log_photos_duplicated': os.path.join(LOGS_PATH, *source_paths_name, 'move', 'duplicated.log'),
    'log_photos_screenshot': os.path.join(LOGS_PATH, *source_paths_name, 'move', 'screenshot.log'),
    'log_photos_organize': os.path.join(LOGS_PATH, *source_paths_name, 'move', 'organize.log'),
    'log_photos_hash': os.path.join(LOGS_PATH, *source_paths_name, 'hash', 'hash.log'),
    'log_photos_error': os.path.join(LOGS_PATH, *source_paths_name, 'error', 'error.log')
}

# 获取图片日期
def get_date_taken(file_path):
    try:
        with open(file_path, 'rb') as f:
            tags = exifread.process_file(f)
            if 'EXIF DateTimeOriginal' in tags:
                date_taken = tags['EXIF DateTimeOriginal']
                date_taken = datetime.datetime.strptime(str(date_taken), '%Y:%m:%d %H:%M:%S')
                return date_taken
            else:
                date_taken = os.path.getmtime(file_path)
                date_taken = datetime.datetime.fromtimestamp(date_taken)
                return date_taken
    except (FileNotFoundError, OSError):
        return None

# 读取并返回文件hash值
def calculate_hash(file_path):
    CHUNK_SIZE = 1024
    hash_obj = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(CHUNK_SIZE), b''):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

# 定义日志级别函数，并返回解释器
def create_logger(log_path, log_name):
    if not os.path.exists(os.path.dirname(log_path)):
        os.makedirs(os.path.dirname(log_path))
    log_handler = RotatingFileHandler(log_path, maxBytes=100*1024*1024, backupCount=5)
    log_formatter = logging.Formatter(f'{asctime} {message}')
    log_handler.setFormatter(log_formatter)
    log = logging.getLogger(log_name)
    log.setLevel(logging.INFO)
    log.addHandler(log_handler)
    return log

def organize_files_by_date(directory, target, min_resolution=(low_res_width_threshold, low_res_height_threshold), min_size_kb=small_size_threshold):
    # 根据配置文件中的文件夹名，在目标路径下创建相应的文件夹
    low_res_folder = os.path.join(target, low_res_folder_name)
    small_size_folder = os.path.join(target, small_size_folder_name)
    duplicated_folder = os.path.join(target, duplicated_folder_name)
    screenshot_folder = os.path.join(target, screenshot_folder_name)
    for folder in [low_res_folder, small_size_folder, duplicated_folder, screenshot_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)
    # 创建数据库（不存在则创建）
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("CREATE TABLE files (filename TEXT, hash TEXT)")
        conn.commit()
        cur.close()
        conn.close()
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if os.path.splitext(filename)[1].lower() in photo_formats or os.path.splitext(filename)[1].lower() in video_formats:
                file_path = os.path.join(dirpath, filename)
                # 对比数据库中hash值，如果哈希值已经存在，就移动到重复文件夹，并记录日志;否则，将文件的哈希值添加到数据库中，并记录日志
                conn = sqlite3.connect(db_path)
                cur = conn.cursor()
                file_hash = calculate_hash(file_path)
                cur.execute("SELECT filename FROM files WHERE hash = ?", (file_hash,))
                result = cur.fetchone()
                if result is not None:
                    duplicated_filename = result[0]
                    shutil.move(file_path, duplicated_folder)
                    log_dict['log_photos_duplicated'].info(f"Duplicated file: {filename}")
                    continue
                else:
                    log_dict['log_photos_hash'].info(f'hash value {file_hash}')
                    cur.execute("INSERT INTO files (filename, hash) VALUES (?, ?)", (filename, file_hash))
                    conn.commit()
                cur.close()
                conn.close()
                # 如果文件名中包含screenshot，就移动到截图文件夹，并记录日志
                if 'screenshot' in filename.lower():
                    destination_file_path = os.path.join(screenshot_folder, filename)
                    if os.path.exists(destination_file_path):
                        continue
                    else:
                        shutil.move(file_path, screenshot_folder)
                        log_dict['log_photos_screenshot'].info(f"Moved screenshot file: {filename} to {screenshot_folder}")
                        continue
                if filename.lower().endswith(tuple(photo_formats)):
                    if filename.lower().endswith(".heic"):
                        heif_file = pyheif.read_heif(file_path)
                        img = Image.frombytes(
                        heif_file.mode, 
                        heif_file.size, 
                        heif_file.data,
                        "raw",
                        heif_file.mode,
                        heif_file.stride,
                        )
                    else: 
                        img = Image.open(file_path)
                    # 如果文件的分辨率低于阈值，就移动到低分辨率文件夹，并记录日志
                    if img.size < min_resolution:
                        destination_file_path = os.path.join(low_res_folder, filename)
                        if os.path.exists(destination_file_path):
                            continue
                        else:
                            shutil.move(file_path, low_res_folder)
                            log_dict['log_photos_low_res'].info(f"Low resolution image: {filename}, resolution: {img.size}")
                            continue
                    # 如果文件的大小低于阈值，就移动到小图片文件夹，并记录日志
                    if os.path.getsize(file_path) < min_size_kb * 1024:
                        destination_file_path = os.path.join(small_size_folder, filename)
                        if os.path.exists(destination_file_path):
                            continue
                        else:
                            shutil.move(file_path, small_size_folder)
                            log_dict['log_photos_small_size'].info(f"Small size image: {filename}, size: {os.path.getsize(file_path) / 1024} KB")
                        continue
                # 获取文件的日期，如果是图片格式，就使用get_date_taken函数，如果是视频格式，就使用os.path.getmtime函数，如果无法获取日期，就跳过后文件，并记录日志
                if filename.lower().endswith(tuple(photo_formats)):
                    date = get_date_taken(file_path)
                else:
                    date = os.path.getmtime(file_path)
                    date = datetime.datetime.fromtimestamp(date)
                if date is None:
                    log_dict['log_photos_error'].info(f"No date found for file: {filename}")
                    continue
                # 重命名文件
                date_str = date.strftime('%Y%m%d-%H%M%S')
                ext = os.path.splitext(filename)[1]
                new_filename = date_str + ext
                # 在目标路径下创建以年份（子文件夹月份）为名的文件夹，如果已经存在则跳过
                year_folder = os.path.join(target, date.strftime('%Y'))
                if not os.path.exists(year_folder):
                    os.makedirs(year_folder)
                month_folder = os.path.join(year_folder, date.strftime('%m'))
                if not os.path.exists(month_folder):
                    os.makedirs(month_folder)
                # 在移动文件之前，检查目标文件夹中是否已经存在相同的文件名，如果存在，就在文件名后面加上一个数字
                new_file_path = os.path.join(month_folder, new_filename)
                if file_hash not in file_hashes:
                    counter = 1
                    while os.path.exists(new_file_path):
                        new_filename = date_str + '-' + str(counter) + ext
                        new_file_path = os.path.join(month_folder, new_filename)
                        counter += 1
                # 移动文件到对应的月份文件夹下，并用新的文件名重命名，并记录日志
                shutil.move(file_path, new_file_path)
                log_dict['log_photos_organize'].info(f"Moved file: {filename} to {month_folder} and renamed to {new_filename}")

# 新增的代码：用一个循环来调用函数，创建日志文件的处理器和记录器
for item, log_path in log_dict.items():
    log_dict[item] = create_logger(log_path, item)

# 检查source_path和target_path长度是否相等，如果不相等，就抛出一个异常，并记录日志
if len(source_paths) != len(target_paths):
    raise ValueError("Source paths and target paths do not match")

# 遍历每个source_path和target_path，调用organize_files_by_date函数
for source, target in zip(source_paths, target_paths):
    db_name = os.path.basename(source) + '.db'
    db_path = os.path.join(DB_FOLDER, db_name)
    organize_files_by_date(source, target)
