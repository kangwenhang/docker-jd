#!/bin/bash

too() {
  echo "载入配置"
  sleep 2
  ln -sf /pagermaid/workdir/config/config.yml /pagermaid/workdir/config.yml
  sleep 2
  ln -sf /pagermaid/workdir/config/pagermaid.session /pagermaid/workdir/pagermaid.session
  sleep 2
  echo never > /sys/kernel/mm/transparent_hugepage/enabled
  sleep 2
  echo "载入完成"
}

if [ -f "/pagermaid/workdir/config/config.yml" -a -f "/pagermaid/workdir/config/pagermaid.session" ];then
  too
  pm2 start 'python3 -m pagermaid' --name tgbot
  nohup bash /pagermaid/workdir/utils/ping.sh >/dev/null 2>&1&
else 
  echo "未检测到配置文件，请使用命令："
  echo "容器外：docker exec -it 容器名称 bash /pagermaid/workdir/utils/docker-run.sh"
  echo "容器内：bash /pagermaid/workdir/utils/docker-run.sh"
fi

tail -f /dev/null

exec "$@"
