#!/bin/bash

too() {
  echo "运行完成后，请进入数据面板配置相关参数，地址：Http://傻妞地址/admin"
  echo "初始用户名：admin"
  echo "初始密码：随机，请查看日志"
  echo "完成后请重启容器，命令：docker restart 容器名称"
  sleep 5
  ./sillyGirl -t
}

if [ -f "/etc/sillyGirl/sets.conf" -a -f "/etc/sillyGirl/sillyGirl.cache" ];then
  echo "检测到配置，开始运行傻妞"
  pm2 start ./sillyGirl
  pm2 log
else 
  echo "未检测到配置文件，请先自行配置相关设置参数，开始首次运行傻妞"
  if [ ! -d "/sillyGirl/plugin/web/admin/" ];then
    echo "数据web管理插件不存在，开始安装"
    7za x /sillyGirl/admin.zip -r -o/sillyGirl/plugin/web/admin/
    echo "数据web管理插件安装成功"
    too
  else
    if [ "`ls -A /sillyGirl/plugin/web/admin/`" = "" ]; then
      echo "数据web管理插件文件夹存在，但内容为空"
      7za x /sillyGirl/admin.zip -r -o/sillyGirl/plugin/web/admin/
      echo "数据web管理插件安装成功"
      too
    else
      echo "数据web管理插件存在，跳过安装"
      too
    fi
  fi
fi

tail -f /dev/null

exec "$@"
