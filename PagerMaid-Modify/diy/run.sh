#!/bin/bash

too() {
  echo "载入配置"
  sleep 2
  ln -sf /pagermaid/workdir/config/config.yml /pagermaid/workdir/config.yml
  sleep 2
  ln -sf /pagermaid/workdir/config/pagermaid.session /pagermaid/workdir/pagermaid.session
  sleep 2
  echo never > /sys/kernel/mm/transparent_hugepage/enabled
  echo 511 > /proc/sys/net/core/somaxconn
  sleep 2
  echo "载入完成"
}

#导入环境变量
if [ ! -f "/pagermaid/workdir/config/env.sh" ]; then
  echo -e "检测到env文件不存在，拷贝文件...\n"
  cp -fv /pagermaid/workdir/utils/env.sh.sample /pagermaid/workdir/config/env.sh
  echo -e "成功拷贝文件env \n"
  source /pagermaid/workdir/config/env.sh
else
  source /pagermaid/workdir/config/env.sh
fi

if [ -f "/pagermaid/workdir/config/config.yml" -a -f "/pagermaid/workdir/config/pagermaid.session" ];then
  too
  if [ -f "/pagermaid/workdir/config/redis.conf" ];then
    pm2 start 'redis-server /pagermaid/workdir/config/redis.conf'
  else
    cp /pagermaid/workdir/redis.conf /pagermaid/workdir/config/redis.conf 
    pm2 start 'redis-server /pagermaid/workdir/config/redis.conf'
  fi
  pm2 start 'python3 -m pagermaid'
  pm2 log
else 
  echo "未检测到配置文件，请使用命令："
  echo "容器外：docker exec -it 容器名称 bash /pagermaid/workdir/utils/docker-run.sh"
  echo "容器内：bash /pagermaid/workdir/utils/docker-run.sh"
fi

tail -f /dev/null

exec "$@"
