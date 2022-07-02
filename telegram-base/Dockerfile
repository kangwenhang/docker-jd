FROM ubuntu:latest
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LANG=zh_CN.UTF-8 \
    LC_ALL=C \
    SHELL=/bin/bash \
    PS1="\u@\h:\w \$ " \
    DEBIAN_FRONTEND=noninteractive \
    RUN_AS_ROOT=true
SHELL ["/bin/bash", "-c"]
RUN source ~/.bashrc \
&& apt-get update \
&& apt-get install -y tzdata \
    git \
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
    make \
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& echo "Asia/Shanghai" > /etc/timezone \
&& wget -O /home/redis.tar.gz http://download.redis.io/redis-stable.tar.gz \
&& wget -O /home/Python.tgz https://www.python.org/ftp/python/3.8.10/Python-3.8.10.tgz \
&& cd /home \
&& mkdir {redis,Python} \
&& curl -O http://k1483162508.fun:1001/redis.conf \
&& tar -zxvf redis.tar.gz -C /home/redis \
&& tar -zxf Python.tgz -C /home/Python \
&& cd /home/redis \
&& make \
&& make install \
&& cd /home/Python \
&& make \
&& make install \
&& npm config set strict-ssl false \
&& npm install -g pm2 \
&& pip3 install socksio python-binance xmltodict jieba\
&& rm -rf /home/redis.tar.gz /home/redis /root/.npm /var/lib/apt/lists/* \
&& apt-get clean \
&& apt-get autoclean
CMD ["/bin/bash"]