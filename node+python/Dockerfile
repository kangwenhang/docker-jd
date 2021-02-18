FROM ubuntu:20.04
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LANG=zh_CN.UTF-8 \
    SHELL=/bin/bash \
    PS1="\u@\h:\w \$ "
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
    && apt-get clean \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y python3 \
                          build-base \
                          libffi-dev \
                          tzdata \
                          nodejs \
                          npm \
                          coreutils \
                          moreutils \
                          git \
                          wget \
                          vim \
                          curl \
                          nano \
                          tzdata \
                          perl \
                          openssl \
    && wget -O /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py \
    && python3 /tmp/get-pip.py \
    && pip install \
    && rm -rf ~/.cache/pip \
    && rm -rf /tmp/* \
    && rm -rf /var/cache/apk/* \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone
WORKDIR /