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
DB_FOLDER = os.path.join(CONFIG_PATH, 'db')

#读取变量文件
config = configparser.ConfigParser()
config.read(os.path.join('/photos', 'config', 'settings.ini'))

# 定义一个函数，它可以遍历/photos/config/db文件夹内的数据库文件
def traverse_db_files(DB_FOLDER):
    # 获取文件夹下的所有文件
    files = os.listdir(DB_FOLDER)
    # 遍历每个文件
    for file in files:
        # 拼接完整的文件路径
        file_path = os.path.join(DB_FOLDER, file)
        # 获取文件的扩展名
        file_ext = os.path.splitext(file)[1]
        # 如果文件是一个数据库文件，即以.db结尾
        if file_ext == ".db":
            # 调用另一个函数，处理数据库文件
            process_db_file(file_path)

# 定义一个函数，它可以处理数据库文件
def process_db_file(db_file):
    # 使用with语句管理数据库的连接和关闭
    with sqlite3.connect(db_file) as conn:
        # 创建一个游标对象
        cursor = conn.cursor()
        # 执行SQL语句，查询所有的文件hash值
        cursor.execute("SELECT file_hash FROM photos")
        # 获取查询结果
        results = cursor.fetchall()
        # 遍历每个文件hash值
        for result in results:
            # 获取文件hash值
            file_hash = result[0]
            # 拼接文件路径，假设文件都在/photos/organized文件夹下
            file_path = os.path.join("/photos/organized", file_hash)
            # 如果文件不存在
            if not os.path.exists(file_path):
                # 执行SQL语句，删除数据库中对应的记录
                cursor.execute("DELETE FROM photos WHERE file_hash = ?", (file_hash,))
                # 提交更改
                conn.commit()

# 调用函数，遍历数据库文件
traverse_db_files(DB_FOLDER)
