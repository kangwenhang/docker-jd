FROM node:alpine
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LANG=zh_CN.UTF-8 \
    SHELL=/bin/bash \
    MUSICN_DIR=/musicn \
    PS1="\u@\h:\w \$ "
WORKDIR $MUSICN_DIR
COPY run.sh /root/run.sh
RUN npm i musicn -g 
CMD ["bash","/root/run.sh"]
