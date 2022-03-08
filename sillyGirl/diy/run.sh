#!/bin/bash

if [ -f "/etc/sillyGirl/sets.conf" -a -f "/etc/sillyGirl/sillyGirl.cache" ];then
  echo "检测到配置，开始运行傻妞"
  pm2 start ./sillyGirl
  pm2 log
else 
  echo "未检测到配置文件，首次运行傻妞"
  cp -rf /sillyGirl/sets.conf.sample /etc/sillyGirl/sets.conf
  sleep 2
  ./sillyGirl -t
  echo "运行完成，请重启容器"
fi

tail -f /dev/null

exec "$@"
