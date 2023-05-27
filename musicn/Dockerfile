FROM node:alpine
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LANG=zh_CN.UTF-8 \
    SHELL=/bin/bash \
    PS1="\u@\h:\w \$ "
WORKDIR /data
COPY run.sh /root/run.sh
RUN npm i musicn -g
CMD ["bash","/root/run.sh"]
