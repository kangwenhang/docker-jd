#!/bin/bash

too() {
  echo "运行完成后，请进入数据面板配置相关参数，地址：Http://傻妞地址/admin"
  echo "初始用户名：admin"
  echo "初始密码：随机，请查看日志"
  echo "完成后请重启容器，命令：docker restart 容器名称"
  sleep 5
  cd /sillyGirl
  ./sillyGirl -t
  echo -e "\n=============================傻妞配置===================================\n"
}

one() {
  echo '开始启动qqbot'
  oicq $botqq
}

oicq_bot() {
  if [ $oicqbot = "true" ]; then
    if [ -f "/root/.oicq/config.js" ]; then
      echo "检测到配置文件，首次启动OICQ进行确认"
      echo "自动匹配到如下QQ号"
      grep -oP '[1-9][0-9]{4,10}:' /root/.oicq/config.js 2>&1 | tee /sillyGirl/qq.log >/dev/null 2>&1
      sed -i 's/://g' /sillyGirl/qq.log
      cat /sillyGirl/qq.log
      botqq=$(cat /sillyGirl/qq.log)
      if [ ! $botqq = "" ] && [ -d "/root/.oicq/$botqq/token" ]; then
        echo "开始启动OICQ"
        one
      else
        echo "登录信息不存在，请检查登录信息"
      fi
    else
      echo "OICQ未检测到配置文件，开始生成默认配置文件"
      cp -rf /sillyGirl/config.js.sample /root/.oicq/config.js
      echo "OICQ配置文件生成完成，请自行修改配置文件"
  else
    echo "已选择不开启OICQ"
  fi
}

echo -e "\n=============================OICQ配置===================================\n"
oicq_bot
echo -e "\n=============================OICQ配置===================================\n"

echo -e "\n=============================傻妞配置===================================\n"
if [ -d "/sillyGirl/plugin/web/admin/" ] && [ ! "`ls -A /sillyGirl/plugin/web/admin/`" = "" ]; then
  echo "数据web管理插件存在，跳过安装"
  too
else
  echo "数据web管理插件不存在，开始安装"
  7za x /sillyGirl/admin.zip -r -o/sillyGirl/plugin/web/admin/
  chmod -R 777 /sillyGirl/plugin/web/admin/
  echo "数据web管理插件安装成功"
  too
fi

