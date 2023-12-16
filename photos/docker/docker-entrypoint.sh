# 这是你的入口点脚本的内容
#!/bin/bash

echo -e "======================1.检测配置文件========================\n"

# 检查工作目录下是否有config文件夹，如果没有则创建
if [ ! -d "/app/config" ]; then
  mkdir /app/config
fi

# 检查工作目录下是否有logs文件夹，如果没有则创建
if [ ! -d "/app/logs" ]; then
  mkdir /app/logs
fi

echo -e "==================2. 启动定时同步（实时）========================\n"
# 在后台执行你的upcron.sh脚本，并把输出显示在控制台上
# 在后台执行你的upcron.sh脚本，不输出任何信息
./upcron.sh > /dev/null 2>&1 &

echo -e "======================3.启动定时========================\n"
# 启动cron服务
cron


# 实时显示test.log文件的内容
tail -f /app/logs/test.log &