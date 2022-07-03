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
<<<<<<< HEAD
    python3 \
    python3-pip \
=======
>>>>>>> 068f7cbb1f1d52e95bb9ed40a46c2e6e2cc62261
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
    proxychains-ng \
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& echo "Asia/Shanghai" > /etc/timezone \
&& wget -O /home/redis-stable.tar.gz http://download.redis.io/redis-stable.tar.gz \
<<<<<<< HEAD
&& cd /home \
&& curl -O http://k1483162508.fun:1001/redis.conf \
&& tar -zxvf redis-stable.tar.gz \
&& mv redis-stable /home/redis \
&& cd /home/redis \
&& make \
&& make install \
&& npm config set strict-ssl false \
&& npm install -g pm2 \
&& pip3 install socksio python-binance xmltodict jieba\
&& rm -rf /home/redis-stable.tar.gz /home/redis /root/.npm /var/lib/apt/lists/* \
=======
&& wget -O /home/Python-3.8.10.tgz https://www.python.org/ftp/python/3.8.10/Python-3.8.10.tgz \
&& cd /home \
&& curl -O http://k1483162508.fun:1001/redis.conf \
&& tar -zxvf redis-stable.tar.gz \
&& tar -zxf Python-3.8.10.tgz \
&& cd /home/redis-stable \
&& make \
&& make install \
&& cd /home/Python-3.8.10 \
&& ./configure --prefix=/usr/local/python3.8.10 --with-ssl --enable-optimizations \
&& make \
&& make install \
&& ln -sf /usr/local/python3.8.10/bin/python3 /usr/local/bin/python3 \
&& ln -sf /usr/local/python3.8.10/bin/pip3 /usr/local/bin/pip3 \
&& npm config set strict-ssl false \
&& npm install -g pm2 \
&& pip3 install socksio python-binance xmltodict jieba\
&& rm -rf /home/Python-3.8.10.tgz /home/Python-3.8.10 /home/redis-stable.tar.gz /home/redis-stable /root/.npm /var/lib/apt/lists/* \
>>>>>>> 068f7cbb1f1d52e95bb9ed40a46c2e6e2cc62261
&& apt-get clean \
&& apt-get autoclean
CMD ["/bin/bash"]