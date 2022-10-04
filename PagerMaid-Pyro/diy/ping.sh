#!/usr/bin/env bash

#自定义变量
path=/pagermaid/workdir/utils
time=80s

# 启动进程
function satrt_pid()
{
    cd $path
    python3 ping.py
}

# 对象对比判断
while :
do
    satrt_pid
    sleep $time
done