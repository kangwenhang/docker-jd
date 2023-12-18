# 使用python:3.9作为基础镜像
FROM python:3.9

# 设置工作目录为/photos
WORKDIR /photos

# 复制你的Python脚本和配置文件到工作目录
COPY docker/docker-entrypoint.sh /photos/

# 复制script文件夹及文件夹下的文件到/photos/script
# Copy the script folder and the files under it to /photos/script
COPY script /photos/script

# 复制sample文件夹及文件夹下的文件到/photos/sample
# Copy the sample folder and the files under it to /photos/sample
COPY sample /photos/sample

# 安装cron，用于定时任务，并修改你的入口点脚本的权限，使其可执行
RUN apt-get update \
    && apt-get install -y cron \
    && chmod +x /photos/docker-entrypoint.sh \
    && pip install Pillow configparser exiftool logging

# 启动你的入口点脚本
ENTRYPOINT ["./docker-entrypoint.sh"]