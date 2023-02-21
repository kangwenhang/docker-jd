#!/usr/bin/env bash

#自定义变量
url="https://www.google.com.hk"
time=80s

# 启动进程
function satrt_pid()
{
    socks5_decide
    pm2_status
    if [[ $agent == "yes" ]]; then
        echo $proxy
        code=`curl --socks5 k1483162508.fun:9000 -I -m 30 -o /dev/null -s -w %{http_code}"\n" $url`
        echo $code
        code_status
    elif [[ $agent == "no" ]] && [[ $mtp_addr == "no" ]]; then
        code=`curl -I -m 30 -o /dev/null -s -w %{http_code}"\n" $url`
        code_status
    else
        echo "...."
    fi
}

function code_status {
    a="stopped"
    b="online"
    if [[ $code == "200" ]]; then
        echo "ok"
        if [[ $pm2status == *$a* ]];then
            pm2 start tgbot
        fi
    else
        echo "no"
        if [[ $pm2status == *$b* ]];then
            pm2 stop tgbot
        fi
    fi
}

function pm2_status {
    pm2status=`pm2 describe tgbot`

}

function socks5_decide {
    desStr1='proxy_addr:'
    desStr2='proxy_port:' 
    desStr3='http_addr:' 
    desStr4='http_port:' 
    desStr5='mtp_addr:'
    j=1
    agent="no"
    mtp_addr="no"
    desStr5=`cat config.yml | grep $desStr5`
    desStr5=`echo $desStr5 | sed -r 's/.*"(.+)".*/\1/'`
    if [[ $desStr5 == 'mtp_addr: ""' ]]; then
        while [[ j -le 3 ]]; do
            Tmp_desStr=desStr$j
            desStr_Tmp=${!Tmp_desStr}
            print_desStr=`cat config.yml | grep $desStr_Tmp`
            print_desStr=`echo $print_desStr | sed -r 's/.*"(.+)".*/\1/'`
            if [[ $print_desStr == 'proxy_addr: ""' ]] || [[ $print_desStr == 'http_addr: ""' ]] ; then
                let j=j+2
            else
                agent="yes"
                let j++
                Tmp_des=desStr$j
                des_Tmp=${!Tmp_des}
                print_des=`cat config.yml | grep $des_Tmp`
                print_des=`echo $print_des| sed -r 's/.*"(.+)".*/\1/'`
                proxy="$print_desStr"":""$print_des"
                break
            fi
        done
    else
        mtp_addr="yes"
    fi
}

# 对象对比判断
while :
do
    satrt_pid
    sleep $time
done