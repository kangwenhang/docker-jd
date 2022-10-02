#!/usr/bin/env bash

#自定义变量
path=/pagermaid/workdir
time=60s

# 判断
while :
do
    cd $path
    pm2 describe tgbot > tgbot.log 2>&1
    if [ "`grep -c "\<timeout\>" $path/ping.log`" -ge "3" ] ; then
        if [ "`grep -c "\<online\>" $path/tgbot.log`" -eq "1" ];then
            echo "代理连接失败，停止bot"
            pm2 stop tgbot
            pm2 restart ping
        else
            echo "代理连接失败，bot已停止，跳过"
            pm2 restart ping
        fi
    else
        if [ "`grep -c "\<stopped\>" $path/tgbot.log`" -eq "1" ]; then
            echo "代理连接成功，开启bot"
            pm2 start 'tgbot'
        else
            echo "代理连接成功，bot未停止，跳过"
        fi
    fi
    sleep $time
done