FROM node:lts-alpine
ENV SHELL=/bin/bash \
    DEBIAN_FRONTEND=noninteractive
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk update -f \
    && apk upgrade \
    && apk --no-cache add -f bash \
                             build-essential \
                             libffi-dev \
                             tzdata \
                             npm \
                             git \
                             wget \
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
                             python3 \
                             python3-dev \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py \
    && pip --no-cache-dir install aiohttp requests wasmtime utils \
    && rm -rf ~/.cache/pip \
    && npm config set strict-ssl false \
    && npm install -g pnpm \
    && rm -rf /root/.npm \
    && rm -rf /tmp/* \
    && rm -rf /var/cache/apk/*
CMD ["/bin/bash"]