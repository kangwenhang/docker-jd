#!/bin/bash
set -e

echo -e "======================1.检测配置文件========================\n"
if [ -s ${dir_root}/config/crontab.list ]
then
  echo -e "检测到config配置目录下存在crontab.list，自动导入定时任务...\n"
  crontab ${dir_root}/config/crontab.list
  echo -e "成功添加定时任务...\n"
else
  echo -e "检测到config配置目录下不存在crontab.list或存在但文件为空，从示例文件复制一份用于初始化...\n"
  cp -fv ${dir_root}/sample/crontab.list.sample ${dir_root}/config/crontab.list
  echo
  crontab ${dir_root}/config/crontab.list
  echo -e "成功添加定时任务...\n"
fi

if [ ! -d "${dir_root}/config/config_model/" ]; then
  echo -e "检测到config_model文件夹不存在，拷贝文件夹...\n"
  cp -rf ${dir_root}/sample/config_model/ ${dir_root}/config/
  echo -e "成功创建文件夹 config_model \n"
fi

if [ ! -d "${dir_root}/logs/" ]; then
  echo -e "检测到log文件夹不存在，创建文件夹...\n"
  mkdir -p ${dir_root}/logs
  echo -e "成功创建文件夹 logs \n"
fi

if [ ! -d "${dir_root}/diy/" ]; then
  echo -e "检测到diy文件夹不存在，创建文件夹...\n"
  mkdir -p ${dir_root}/diy
  echo -e "成功创建文件夹 diy \n"
fi

if [ ! -d "${dir_root}/backup/old/" ]; then
  echo -e "检测到/backup/old文件夹不存在，创建文件夹...\n"
  mkdir -p ${dir_root}/backup/old
  echo -e "成功创建文件夹 backup/old \n"
fi

if [ ! -d "${dir_root}/backup/raw/" ]; then
  echo -e "检测到/backup/raw文件夹不存在，创建文件夹...\n"
  mkdir -p ${dir_root}/backup/raw
  echo -e "成功创建文件夹 backup/raw \n"
fi

echo -e "==================2. 启动定时同步（实时）========================\n"
cd ${dir_root}/shell
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
