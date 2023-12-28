FROM python:alpine3.19
ENV LANG=zh_CN.UTF-8 \
    LC_ALL=C \
    SHELL=/bin/bash \
    PS1="\u@\h:\w \$ " \
    dir_root=/photos
WORKDIR ${dir_root}
COPY docker/docker-entrypoint.sh ${dir_root}/docker-entrypoint.sh
COPY script /photos/script
COPY sample /photos/sample
RUN apk add --no-cache bash git curl wget tzdata tar jq vim nodejs npm \
    && npm config set strict-ssl false \
    && npm install -g pm2 \
    && pip install setuptools pillow configparser pyexiftool pyheif exifread==2.3.2 \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && ln -sf /bin/bash /bin/sh \
    && chmod +x ${dir_root}/docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
