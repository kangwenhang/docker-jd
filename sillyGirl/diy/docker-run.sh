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
      if [ ! $botqq = "" ] && [ -f "/root/.oicq/$botqq/token" ] || [ -f "/root/.oicq/$botqq/token.sample" ]; then
        echo "配置信息存在。跳过此项部署"
      else
        echo "配置信息不存在，开始启动OICQ"
        one
      fi
    else
      echo "OICQ未检测到配置文件，开始生成默认配置文件"
      cp -rf /sillyGirl/config.js.sample /root/.oicq/config.js
      echo "OICQ配置文件生成完成，请自行修改配置文件。文件地址：映射地址oicq"
      echo "修改完成后继续运行：bash /sillyGirl/docker-run.sh 此命令"
    fi
  else
    echo "已选择不开启OICQ"
  fi
}

echo -e "\n=============================OICQ配置===================================\n"
oicq_bot
if [ $oicqbot = "true" ] && [ -f "/root/.oicq/$botqq/token" ]; then
  echo "检测到配置完成，备份token文件"
  cp -rf /root/.oicq/$botqq/token /root/.oicq/$botqq/token.sample
  echo "备份结束"
fi
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

