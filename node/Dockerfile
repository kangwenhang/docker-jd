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
                      openssl \
                      net-tools \
                      nodejs-legacy \
                      npm \
                      vim \    
                      curl \
                      wget \
                      sudo \
                      p7zip-full \
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& echo "Asia/Shanghai" > /etc/timezone \
&& npm install npm@latest -g \
&& npm config set strict-ssl false \
&& npm install -g pm2 \
&& sudo n stable \
&& rm -rf /root/.npm \
&& apt-get clean \
&& apt-get autoclean \
&& rm -rf /var/lib/apt/lists/*
CMD ["/bin/bash"]