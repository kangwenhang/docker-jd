# 导入所需的模块
import os
import sqlite3
import hashlib
import configparser

# 定义常量
ROOT_PATH = '/photos'
CONFIG_PATH = os.path.join(ROOT_PATH, 'config')
LOGS_PATH = os.path.join(ROOT_PATH, 'logs')
PHOTOS_PATH = os.path.join(ROOT_PATH, 'data')

#读取变量文件
config = configparser.ConfigParser()
config.read(os.path.join('/photos', 'config', 'settings.ini'))

# 从变量文件中获取source_paths和target_paths的值，它们是以逗号分隔的字符串
source_paths = config.get('paths', 'source_paths').split(',')
target_paths = config.get('paths', 'target_paths').split(',')

# 定义一个函数，它可以遍历source_paths中的数据库文件
def traverse_db_files(source_paths):
    # 遍历每个数据库文件的名称
    for db_name in source_paths:
        # 拼接完整的文件路径，加上/photos/config/db文件夹和.db扩展名
        db_file = os.path.join(CONFIG_PATH, 'db', db_name + '.db')
        # 如果文件存在
        if os.path.exists(db_file):
            # 调用另一个函数，处理数据库文件
            process_db_file(db_file, db_name)

# 定义一个函数，它可以处理数据库文件
def process_db_file(db_file, db_name):
    # 使用with语句管理数据库的连接和关闭
    with sqlite3.connect(db_file) as conn:
        # 创建一个游标对象
        cursor = conn.cursor()
        # 执行SQL语句，查询所有的文件hash值
        cursor.execute("SELECT file_hash FROM photos")
        # 获取查询结果
        results = cursor.fetchall()
        # 将查询结果转换为一个集合，方便后续的比较
        db_hashes = set([result[0] for result in results])
        # 根据数据库文件的名称，找到对应的对比文件夹的名称，它们在source_paths和target_paths中的位置相同
        target_path = target_paths[source_paths.index(db_name)]
        # 获取对比文件夹下的所有文件
        files = os.listdir(os.path.join(PHOTOS_PATH, target_path))
        # 定义一个空集合，用于存储对比文件夹中的文件hash值
        folder_hashes = set()
        # 遍历每个文件
        for file in files:
            # 拼接完整的文件路径
            file_path = os.path.join(PHOTOS_PATH, target_path, file)
            # 计算文件的hash值，使用md5算法
            file_hash = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
            # 将文件的hash值添加到集合中
            folder_hashes.add(file_hash)
        # 比较数据库中的hash值和对比文件夹中的hash值，找出需要删除和添加的hash值
        hashes_to_delete = db_hashes - folder_hashes
        hashes_to_add = folder_hashes - db_hashes
        # 遍历每个需要删除的hash值
        for hash_to_delete in hashes_to_delete:
            # 执行SQL语句，删除数据库中对应的记录
            cursor.execute("DELETE FROM photos WHERE file_hash = ?", (hash_to_delete,))
            # 提交更改
            conn.commit()
        # 遍历每个需要添加的hash值
        for hash_to_add in hashes_to_add:
            # 执行SQL语句，插入数据库中对应的记录，假设文件名和hash值相同
            cursor.execute("INSERT INTO photos (file_name, file_hash) VALUES (?, ?)", (hash_to_add, hash_to_add))
            # 提交更改
            conn.commit()

# 调用函数，遍历数据库文件
traverse_db_files(source_paths)
