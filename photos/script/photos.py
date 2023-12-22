#!/usr/bin/env python3
import os
import shutil
from PIL import Image
import datetime
import hashlib # 导入hashlib库，用于计算文件的哈希值
import configparser # 导入configparser库，用于读写ini文件
import logging # 导入logging库，用于记录日志
import exifread # 导入exifread库
import pyheif # 导入pyheif库

#定义常量
EXIF_DATE_TIME_ORIGINAL = 36867

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
log_path = os.path.join('/photos', 'logs', 'organize.log')
source_paths = config.get('paths', 'source_paths').split(',')
target_paths = config.get('paths', 'target_paths').split(',')

def get_date_taken(file_path):
    try:
        with open(file_path, 'rb') as f:
            # 获取图片的元数据
            tags = exifread.process_file(f)
            # 如果元数据存在，查找EXIF DateTimeOriginal的键值
            if 'EXIF DateTimeOriginal' in tags:
                date_taken = tags['EXIF DateTimeOriginal']
                # 将日期转换为datetime对象
                date_taken = datetime.datetime.strptime(str(date_taken), '%Y:%m:%d %H:%M:%S')
                return date_taken
            else:
                date_taken = os.path.getmtime(file_path)
                # 将日期转换为datetime对象
                date_taken = datetime.datetime.fromtimestamp(date_taken)
                return date_taken
    # 使用contextlib.suppress来忽略特定的异常
    except (FileNotFoundError, OSError):
        return None

def calculate_hash(file_path):
    # Define a chunk size
    CHUNK_SIZE = 1024
    # Create a hash object
    hash_obj = hashlib.md5()
    with open(file_path, 'rb') as f:
        # Read a chunk of data
        chunk = f.read(CHUNK_SIZE)
        # Loop until the end of the file
        while chunk:
            # Update the hash value
            hash_obj.update(chunk)
            # Read the next chunk
            chunk = f.read(CHUNK_SIZE)
    # Return the readable hash value
    return hash_obj.hexdigest()

def organize_files_by_date(directory, target, min_resolution=(low_res_width_threshold, low_res_height_threshold), min_size_kb=small_size_threshold):
    file_hashes = set()
    # 根据配置文件中的文件夹名，在目标路径下创建相应的文件夹
    low_res_folder = os.path.join(target, low_res_folder_name)
    small_size_folder = os.path.join(target, small_size_folder_name)
    duplicated_folder = os.path.join(target, duplicated_folder_name)
    screenshot_folder = os.path.join(target, screenshot_folder_name)
    for folder in [low_res_folder, small_size_folder, duplicated_folder, screenshot_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)
    # 配置logging模块，设置日志级别为INFO，日志格式为时间+消息，日志文件名为log_path，日志模式为追加,在配置logging模块之前，检查log_path是否存在，如果不存在，就创建它
    if not os.path.exists(log_path):
        open(log_path, 'w').close()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', filename=log_path, filemode='a')
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            # 使用or运算符来代替+运算符
            if os.path.splitext(filename)[1].lower() in photo_formats or os.path.splitext(filename)[1].lower() in video_formats:
                file_path = os.path.join(dirpath, filename)
                file_hash = calculate_hash(file_path)
                # 如果文件名中包含screenshot，就移动到截图文件夹，并记录日志
                if 'screenshot' in filename.lower():
                    shutil.move(file_path, screenshot_folder)
                    logging.info(f"Moved screenshot file: {filename} to {screenshot_folder}")
                    continue
                # 如果文件的哈希值已经存在，就移动到重复文件夹，并记录日志
                if file_hash in file_hashes:
                    logging.info(f"Duplicated file: {filename}")
                    shutil.move(file_path, duplicated_folder)
                    continue
                # 否则，将文件的哈希值添加到集合中
                file_hashes.add(file_hash)
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
                        logging.info(f"Low resolution image: {filename}, resolution: {img.size}")
                        shutil.move(file_path, low_res_folder)
                        continue
                    # 如果文件的大小低于阈值，就移动到小图片文件夹，并记录日志
                    if os.path.getsize(file_path) < min_size_kb * 1024:
                        logging.info(f"Small size image: {filename}, size: {os.path.getsize(file_path) / 1024} KB")
                        shutil.move(file_path, small_size_folder)
                        continue
                # 获取文件的日期，如果是图片格式，就使用get_date_taken函数，如果是视频格式，就使用os.path.getmtime函数
                if filename.lower().endswith(tuple(photo_formats)):
                    date = get_date_taken(file_path)
                else:
                    date = os.path.getmtime(file_path)
                # 如果无法获取日期，就跳过后面的代码，直接移动文件到错误文件夹，并记录日志 # 修改
                if date is None:
                    logging.info(f"No date found for file: {filename}")
                    continue
                # 格式化日期为YYYYMMDD-HHMMSS的形式
                date_str = date.strftime('%Y%m%d-%H%M%S')
                # 获取文件的扩展名
                ext = os.path.splitext(filename)[1]
                # 用日期字符串和扩展名拼接新的文件名
                new_filename = date_str + ext
                # 在目标路径下创建以年份为名的文件夹，如果已经存在则跳过
                year_folder = os.path.join(target, date.strftime('%Y'))
                if not os.path.exists(year_folder):
                    os.makedirs(year_folder)
                # 在年份文件夹下创建以月份为名的文件夹，如果已经存在则跳过
                month_folder = os.path.join(year_folder, date.strftime('%m'))
                if not os.path.exists(month_folder):
                    os.makedirs(month_folder)
                # 在移动文件之前，检查目标文件夹中是否已经存在相同的文件名，如果存在，就在文件名后面加上一个数字
                new_file_path = os.path.join(month_folder, new_filename)
                counter = 1
                while os.path.exists(new_file_path):
                    # 在文件名和扩展名之间加上一个数字
                    new_filename = date_str + '-' + str(counter) + ext
                    new_file_path = os.path.join(month_folder, new_filename)
                    counter += 1
                # 移动文件到对应的月份文件夹下，并用新的文件名重命名，并记录日志
                shutil.move(file_path, new_file_path)
                logging.info(f"Moved file: {filename} to {month_folder} and renamed to {new_filename}")

# 检查source_path和target_path长度是否相等，如果不相等，就抛出一个异常，并记录日志
if len(source_paths) != len(target_paths):
    logging.error(f"Source paths and target paths do not match: {source_paths}, {target_paths}")
    raise ValueError("Source paths and target paths do not match")

# 遍历每个source_path和target_path，调用organize_files_by_date函数
for source, target in zip(source_paths, target_paths):
    organize_files_by_date(source, target)
