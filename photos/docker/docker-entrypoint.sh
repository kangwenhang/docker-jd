#!/bin/bash

echo -e "======================1.检测配置文件========================\n"
if [ ! -d "/photos/config/" ]; then
  echo -e "检测到config文件夹不存在，创建文件夹...\n"
  mkdir -p /photos/config/
  echo -e "成功创建文件夹 config \n"
fi

if [ ! -d "/photos/logs/" ]; then
  echo -e "检测到log文件夹不存在，创建文件夹...\n"
  mkdir -p /photos/logs/
  echo -e "成功创建文件夹 logs \n"
fi

if [ -s /photos/config/crontab.list ]
then
  echo -e "检测到config配置目录下存在crontab.list，自动导入定时任务...\n"
  crontab /photos/config/crontab.list
  echo -e "成功添加定时任务...\n"
else
  echo -e "检测到config配置目录下不存在crontab.list或存在但文件为空，从示例文件复制一份用于初始化...\n"
  cp -fv /photos/sample/crontab.list.sample /photos/config/crontab.list
  echo
  crontab /photos/config/crontab.list
  echo -e "成功添加定时任务...\n"
fi

if [ -s /photos/config/settings.ini ]
then
  echo -e "检测到config配置目录下存在settings.ini，跳过...\n"
else
  echo -e "检测到config配置目录下不存在settings.ini或存在但文件为空，从示例文件复制一份用于初始化...\n"
  cp -fv /photos/sample/settings.ini.sample /photos/config/settings.ini
  echo -e "成功添加变量文件...\n"
fi

echo -e "==================2. 启动定时同步（实时）========================\n"
cd /photos/script
pm2 start 'bash upcron.sh'
echo -e "定时同步启动成功...\n"

echo -e "======================3.启动定时========================\n"
: > /var/log/cron.log
rm -rf /run/rsyslogd.pid
rm -rf /var/run/crond.pid
service rsyslog start
service cron start
tail -f /var/log/cron.log

exec "$@"
