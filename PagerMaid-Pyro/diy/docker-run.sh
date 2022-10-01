#!/bin/bash

welcome() {
  echo ""
  echo "欢迎进入 PagerMaid-Pyro Docker 。"
  echo "配置即将开始"
  echo ""
  sleep 2
}

configure() {
  cd /pagermaid/workdir
  config_file=/pagermaid/workdir/config/config.yml
  if [ -e "$config_file" ];then
    ln -sf $config_file /pagermaid/workdir/config.yml
    echo "配置文件存在，跳过此引导，进行下一步"
    return
  else
    echo "配置文件不存在，生成配置文件中 . . ."
    cp config.gen.yml $config_file
    echo "api_id、api_hash 申请地址： https://my.telegram.org/"
    printf "请输入应用程序 api_id："
    read -r api_id <&1
    sed -i "s/ID_HERE/$api_id/" $config_file
    printf "请输入应用程序 api_hash："
    read -r api_hash <&1
    sed -i "s/HASH_HERE/$api_hash/" $config_file
    printf "请输入应用程序语言（默认：zh-cn）："
    read -r application_language <&1
    if [ -z "$application_language" ]
    then
      echo "语言设置为 简体中文"
    else
      sed -i "s/zh-cn/$application_language/" $config_file
    fi
    printf "请输入应用程序地区（默认：China）："
    read -r application_region <&1
    if [ -z "$application_region" ]
    then
      echo "地区设置为 中国"
    else
      sed -i "s/China/$application_region/" $config_file
    fi
    printf "启用日志记录？ [Y/n]"
    read -r logging_confirmation <&1
    case $logging_confirmation in
      [yY][eE][sS]|[yY])
        printf "请输入您的日志记录群组/频道的 ChatID （如果要发送给 原 PagerMaid 作者 ，请按Enter）："
        read -r log_chatid <&1
        if [ -z "$log_chatid" ]
        then
          echo "LOG 将发送到 原 PagerMaid 作者."
        else
          sed -i "s/503691334/$log_chatid/" $config_file
        fi
        sed -i "s/log: False/log: True/" $config_file
        ln -sf $config_file /pagermaid/workdir/config.yml
        ;;
      [nN][oO]|[nN])
        echo "安装过程继续 . . ."
        ln -sf $config_file /pagermaid/workdir/config.yml
        ;;
      *)
        echo "输入错误 . . ."
        exit 1
        ;;
    esac
  fi
}

login() {
  echo ""
  echo "下面进行程序运行。"
  echo "注意：请在账户授权完毕后，按 Ctrl + C 退出配置界面并重启容器pagermaid。"
  echo "重启命令为docker restart 容器名称"
  echo ""
  sleep 2
  if [ -e "/pagermaid/workdir/config/pagermaid.session" ];then
    echo "tg个人信息文件存在，跳过此配置，结束"
    exit
  else
    python3 -m pagermaid
    if [ $? = 0 ]; then
      cp -rf /pagermaid/workdir/pagermaid.session /pagermaid/workdir/config/pagermaid.session
      rm -rf /pagermaid/workdir/pagermaid.session
      exit
    else
      exit
    fi
  fi
}

start_installation() {
  welcome
  configure
  login
}

start_installation
