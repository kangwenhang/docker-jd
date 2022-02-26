FROM ubuntu:latest
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LANG=zh_CN.UTF-8 \
    LC_ALL=C \
    SHELL=/bin/bash \
    PS1="\u@\h:\w \$ "
SHELL ["/bin/bash", "-c"]
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
&& cd /pagermaid/workdir \
&& npm install -g pm2 \
&& rm -rf /root/.npm \
&& apt-get clean \
&& apt-get autoclean \
&& rm -rf /var/lib/apt/lists/*
CMD ["/bin/bash"]