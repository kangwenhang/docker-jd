# 这是你的入口点脚本的内容
#!/bin/bash

echo -e "======================1.检测配置文件========================\n"

# 检查工作目录下是否有config文件夹，如果没有则创建
if [ ! -d "/photos/config" ]; then
  mkdir /photos/config
fi

# 检查工作目录下是否有logs文件夹，如果没有则创建
if [ ! -d "/photos/logs" ]; then
  mkdir /photos/logs
fi

# 检查工作目录下是否有settings.ini文件，如果没有则从/app/config文件夹中复制
# Check if there is a settings.ini file in the working directory, and copy it from /app/config folder if not
cp -n /photos/sample/settings.ini.sample /photos/config/settings.ini
cp -n /photos/sample/crontab.list.sample /photos/config/crontab.list

echo -e "==================2. 启动定时同步（实时）========================\n"
# 在后台执行你的upcron.sh脚本，不输出任何信息
./shcript/upcron.sh > /dev/null 2>&1 &

echo -e "======================3.启动定时========================\n"
# 启动cron服务
cron

# 实时显示test.log文件的内容
tail -f /app/logs/test.log &