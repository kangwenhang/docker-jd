#!/usr/bin/env bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin 

## 通用变脸
dir_root=/push
shell=$dir_root/shell
shell_model=$shell/model
logs=$dir_root/logs
config=$dir_root/config
diy_logs=$logs/$config_use
log_time=$(date "+%Y-%m-%d-%H-%M-%S.%N")
log_path="$diy_logs/$log_time.log"
ListCron=$config/crontab.list
submit=$diy_logs/sd/submit

#push专用变量
diy_config=$dir_root/diy/$config_use
dir_repo=$dir_root/repo/$config_use
dir_backup=$dir_root/backup
dir_backup_raw=$dir_backup/raw
old_backup=$dir_backup/old
dir_sample=$dir_root/sample
dir_raw=$dir_root/raw
raw_flie=$dir_raw/$config_use
tongbu=$dir_root/temporary_file/$config_use
tongbu_push=$tongbu/sd/push
tongbu_temp=$tongbu/sd/temp
file_config=$config/$config_use/config.sh
file_diyreplace=$config/$config_use/diyreplace.sh
file_gitignore=$config/$config_use/.gitignore
