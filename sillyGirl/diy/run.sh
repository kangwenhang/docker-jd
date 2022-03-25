#!/bin/bash

oicq_bot () {
  if [ $oicqbot = "true" ]; then
    if [ -f "/root/.oicq/config.js" ]; then
      echo "检测到配置文件，开始启动qqbot"
      echo "自动匹配到如下QQ号"
      grep -oP '[1-9][0-9]{4,10}:' /root/.oicq/config.js 2>&1 | tee /sillyGirl/qq.log >/dev/null 2>&1
      if [[ `cat /sillyGirl/qq.log | wc -l` -eq 0 ]]; then
        echo "错误！未检测到QQ号，请确认配置是否已填写"
        return
      else
        sed -i 's/://g' /sillyGirl/qq.log
        cat /sillyGirl/qq.log
        botqq=$(cat /sillyGirl/qq.log)
        if [ -d "/root/.oicq/$botqq/token" ]; then
          echo "开始启动oicq"
          pm2 start "oicq $botqq"
          return
        else
          echo "登录信息不存在，请检查登录信息"
          return
        fi
      fi
    else
      echo "OICQ未检测到配置文件，请使用命令："
      echo "容器外：docker exec -it 容器名称 bash /sillyGirl/docker-run.sh"
      echo "容器内：bash /sillyGirl/docker-run.sh"
    fi
  else
    echo "已选择不开启oicq"
  fi
}

oicq_bot
if [ -f "/etc/sillyGirl/sillyGirl.cache" ]; then
  if [ -d "/sillyGirl/plugin/web/admin/" ] && [ ! "`ls -A /sillyGirl/plugin/web/admin/`" = "" ]; then
    echo "检测到配置，开始运行傻妞"
    cd /sillyGirl
    pm2 start ./sillyGirl
    pm2 log
  else
    echo "面板异常，开始恢复面板"
    7za x /sillyGirl/admin.zip -r -o/sillyGirl/plugin/web/admin/
    chmod -R 777 /sillyGirl/plugin/web/admin/
    echo "面板恢复成功，开始启动傻妞"
    cd /sillyGirl
    pm2 start ./sillyGirl
    pm2 log
  fi
else
  echo "sillyGirl未检测到配置文件，请使用命令："
  echo "容器外：docker exec -it 容器名称 bash /sillyGirl/docker-run.sh"
  echo "容器内：bash /sillyGirl/docker-run.sh"
fi

tail -f /dev/null

exec "$@"
