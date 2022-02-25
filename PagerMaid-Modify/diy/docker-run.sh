#!/bin/bash

too() {
  echo "载入配置"
  sleep 2
  cp -rf /pagermaid/workdir/config/config.yml /pagermaid/workdir/config.yml
  sleep 2
  cp -rf /pagermaid/workdir/config/pagermaid.session /pagermaid/workdir/pagermaid.session
  sleep 2
  echo "载入完成"
}

if [ -f "/pagermaid/workdir/config/config.yml" -a -f "/pagermaid/workdir/config/pagermaid.session" ];then
  too
  pm2 start redis-server &
  python3 -m pagermaid
else 
  echo "配置文件不存在，请进容器手动执行:bash /pagermaid/workdir/utils/run.sh"
fi
