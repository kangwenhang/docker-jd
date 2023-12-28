# 第一个构建阶段，用来安装和下载一些软件包和文件
FROM ubuntu:24.04 AS builder
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y curl gcc libssl-dev libjpeg-dev zlib1g-dev libffi-dev libheif-dev libde265-dev xz-utils python3 \
    && curl -O https://nodejs.org/dist/v16.13.0/node-v16.13.0-linux-x64.tar.xz \
    && tar xJf node-v16.13.0-linux-x64.tar.xz && mv node-v16.13.0-linux-x64 /opt/node \
    && curl -O https://bootstrap.pypa.io/get-pip.py \
    && mv /usr/lib/python3.11/EXTERNALLY-MANAGED /usr/lib/python3.11/EXTERNALLY-MANAGED.bk \
    && python3 get-pip.py && rm get-pip.py \
    && pip install setuptools pillow configparser pyexiftool pyheif exifread==2.3.2 \
    && apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# 第二个构建阶段，用来运行Python脚本和Node.js应用
FROM alpine:3.14
ENV LANG=zh_CN.UTF-8 \
    LC_ALL=C \
    SHELL=/bin/bash \
    PS1="\u@\h:\w \$ " \
    dir_root=/photos
WORKDIR ${dir_root}
COPY --from=builder /opt/node /opt/node
ENV PATH=/opt/node/bin:$PATH
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/local/lib /usr/local/lib
COPY docker/docker-entrypoint.sh ${dir_root}/docker-entrypoint.sh
COPY script /photos/script
COPY sample /photos/sample
RUN apk add --no-cache bash git curl wget tzdata tar jq vim \
    && npm config set strict-ssl false \
    && npm install -g pm2 \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && ln -sf /bin/bash /bin/sh \
    && chmod +x ${dir_root}/docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
