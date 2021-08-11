FROM python:3.8.11-alpine3.13
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LANG=zh_CN.UTF-8 \
    LC_ALL=C \
    SHELL=/bin/bash \
    JD_DIR=/jd \
    QL_DIR=/ql \
    DEBIAN_FRONTEND=noninteractive \
    PS1="\u@\h:\w \$ "
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk update -f \
    && apk upgrade \
    && apk --no-cache add -f bash \
                             build-essential \
                             libffi-dev \
                             tzdata \
                             nodejs \
                             npm \
                             git \
                             wget \
                             sudo \
                             curl \
                             nano \
                             perl \
                             nginx \
                             coreutils \
                             moreutils \
                             make \
                             gcc \
                             g++ \
                             yarn \
                             libc-dev \
                             musl-dev \
                             musl \
                             autoconf \ 
                             libtool \
                             openssh \
                             openssl \
                             jq \
                             alpine-sdk \
                             build-essential \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && pip --no-cache-dir install aiohttp requests wasmtime utils \
    && rm -rf ~/.cache/pip \
    && npm config set strict-ssl false \
    && npm install -g pnpm \
    && rm -rf /root/.npm \
    && rm -rf /tmp/* \
    && rm -rf /var/cache/apk/*
WORKDIR /