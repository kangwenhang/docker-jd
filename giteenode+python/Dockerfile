FROM python:3.6.13-alpine
ARG JD_BASE_URL=git@gitee.com:lxk0301/jd_scripts.git
ARG JD_BASE_BRANCH=master
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LANG=zh_CN.UTF-8 \
    SHELL=/bin/bash \
    PS1="\u@\h:\w \$ "
COPY ~/id_rsa /root
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk update -f \
    && apk upgrade \
    && apk --no-cache add -f bash \
                             tzdata \
                             nodejs \
                             npm \
                             git \
                             wget \
                             curl \
                             nano \
                             perl \
                             openssl \
                             make \
                             gcc \
                             g++ \
                             libc-dev \
                             musl-dev \
                             musl \
                             autoconf \ 
                             libtool \
                             openssh \
    && pip --no-cache-dir install aiohttp requests wasmtime \
    && rm -rf ~/.cache/pip \
    && rm -rf /tmp/* \
    && rm -rf /var/cache/apk/* \
    && mkdir -p /root/.ssh \
    && mv /root/id_rsa /root/.ssh/ \
    && chmod 600 /root/.ssh/id_rsa \
    && git clone -b ${JD_BASE_BRANCH} ${JD_BASE_URL} ${JD_DIR} \
    && apk del libffi-dev build-base \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone
WORKDIR /