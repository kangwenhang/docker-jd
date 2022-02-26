FROM ubuntu:latest
ARG S6_VERSION=v2.2.0.3
ARG S6_ARCH=amd64
ARG WORK_DIR=/pagermaid/workdir
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LANG=zh_CN.UTF-8 \
    LC_ALL=C \
    SHELL=/bin/bash \
    PS1="\u@\h:\w \$ " \
    DEBIAN_FRONTEND=noninteractive \
    RUN_AS_ROOT=true
SHELL ["/bin/bash", "-c"]
COPY /PagerMaid-Modify/diy/ /root/diy/
WORKDIR $WORK_DIR
RUN source ~/.bashrc \
&& apt-get update \
&& apt-get install -y tzdata \
    git \
    python3 \
    python3-pip \
    imagemagick \
    libzbar-dev \
    fortune-mod \
    neofetch \
    tesseract-ocr \
    gdebi \
    ffmpeg \
    file \
    net-tools \
    iputils-ping \
    iproute2 \
    apt-utils \
    openssl \
    nodejs \
    npm \
    bzip2 \
    sqlite \
    figlet \
    redis \
    curl \
    wget \
    sudo \
    vim \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libevent-dev \
    libffi-dev \
    gcc \
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& echo "Asia/Shanghai" > /etc/timezone \
&& sed -e 's;^# \(%wheel.*NOPASSWD.*\);\1;g' -i /etc/sudoers \
&& mkdir -p /pagermaid/workdir \
&& curl -L -o /tmp/s6-overlay-installer https://github.com/just-containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-${S6_ARCH}-installer \
&& chmod +x /tmp/s6-overlay-installer \
&& /tmp/s6-overlay-installer / \
&& git clone -b master https://gitlab.com/Xtao-Labs/pagermaid-modify.git /pagermaid/workdir \
&& git config --global pull.ff only \
&& cp -r s6/* / \
&& mv -f /root/diy/docker-run.sh /pagermaid/workdir/utils/docker-run.sh \
&& cd /pagermaid/workdir \
&& npm install -g pm2 \
&& pip3 install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt \
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& rm -rf /root/.npm \
&& apt-get clean \
&& apt-get autoclean \
&& rm -rf /var/lib/apt/lists/*
ENTRYPOINT ["/init"]