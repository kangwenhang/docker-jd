#!/usr/bin/env bash

#导入变量
ListCron=/photos/config/crontab.list
md5=package_md5

# 创建md5的函数
function creatmd5()
{
    printf "%s\n" "$package_md5_new" > "$md5"
}

# 判断文件是否存在
if [[ ! -f $md5 ]] ; then
    printf "md5file is not exsit,create md5file.......\n"
    creatmd5
    exit
fi

# 对象对比判断
# 捕捉信号
trap 'printf "Script interrupted\n"; exit' SIGINT SIGTERM
while :
do
    package_md5_new=$(md5sum -b "${ListCron}" | awk '{print $1}'|sed 's/ //g')
    package_md5_old=$(< "$md5"|sed 's/ //g')
    printf "%s\n" "$package_md5_new"
    printf "%s\n" "$package_md5_old"
    if [[ "$package_md5_new" == "$package_md5_old" ]]; then
        printf "\n"
    else
        printf "定时变动\n"
        creatmd5
        crontab "${ListCron}"
    fi
    sleep 2s
done