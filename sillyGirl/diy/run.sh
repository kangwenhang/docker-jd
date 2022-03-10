#!/bin/bash

if [ -f "/etc/sillyGirl/sets.conf" -a -f "/etc/sillyGirl/sillyGirl.cache" ];then
  echo "检测到配置，开始运行傻妞"
  pm2 start ./sillyGirl
  pm2 log
else 
  echo "未检测到配置文件，请先自行配置相关设置参数"
  7za x /sillyGirl/admin.zip -r -o/sillyGirl/plugin/web/admin/
  cp -rf /sillyGirl/sets.conf.sample /etc/sillyGirl/sets.conf
  sleep 2
  ./sillyGirl -t
  echo "运行完成，请进入数据面板配置相关参数，地址：Http://傻妞地址/admin"
  echo "初始用户名：admin"
  echo "初始密码：admin"
  echo "完成后请重启容器，命令：docker restart 容器名称"
fi

tail -f /dev/null

exec "$@"
