#!/bin/bash

too() {
  echo "运行完成后，请进入数据面板配置相关参数，地址：Http://傻妞地址/admin"
  echo "初始用户名：admin"
  echo "初始密码：随机，请查看日志"
  echo "完成后请重启容器，命令：docker restart 容器名称"
  sleep 5
  cd /sillyGirl
  ./sillyGirl -t
}

oicq() {
  if [ $oicqbot = "true" ]; then
    if [ -f "/root/.oicq/config.js" ]; then
      echo "检测到配置文件，首次启动oicq进行确认"
      echo "自动匹配到如下QQ号"
      grep -oP '[1-9][0-9]{4,10}:' /root/.oicq/config.js 2>&1 | tee /sillyGirl/qq.log >/dev/null 2>&1
      sed -i 's/://g' /sillyGirl/qq.log
      cat /sillyGirl/qq.log
      botqq=$(cat /sillyGirl/qq.log)
      if [[ $botqq = "" ]]; then
        echo "错误！未检测到QQ号，请确认配置是否已填写"
        return
      else
        echo "开始启动oicq"
        oicq $botqq
      fi
    else
      echo "未检测到配置文件，开始生成默认配置文件"
      cp -rf /sillyGirl/config.js.sample /root/.oicq/config.js
      echo "生成完成，请自行修改配置文件"
    fi
  else
    echo "已选择不开启oicq"
  fi
}

oicq
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

