FROM node:alpine
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LANG=zh_CN.UTF-8 \
    SHELL=/bin/bash \
    MUSICN_DIR=/musicn \
    PS1="\u@\h:\w \$ "
WORKDIR $MUSICN_DIR
COPY run.sh /root/run.sh
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk update -f \
    && apk upgrade \
    && apk --no-cache add -f git \
    && git clone -b main https://github.com/zonemeen/musicn.git $MUSICN_DIR \
    && cd musicn \
    && npm install \
    && npm run build
CMD ["node","./bin/cli.js"," --qrcode"]
