# 使用python:3.9作为基础镜像

# 设置工作目录为/photos
WORKDIR /photos

# 复制你的Python脚本和配置文件到工作目录
COPY photos.py settings.ini /photos/

# 安装cron，用于定时任务
RUN apt-get install -y cron

# 复制你的入口点脚本到工作目录
COPY docker-entrypoint.sh /photos/

# 修改你的入口点脚本的权限，使其可执行
RUN chmod +x /photos/docker-entrypoint.sh

# 启动你的入口点脚本
ENTRYPOINT ["./docker-entrypoint.sh"]