FROM ubuntu:20.10
ARG kwjKEY="-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAue87XSOSqLP4TckN7ttO7nx0nJ80KAOeq/FgsYBIB8vy+jjq\n2VWyBIa1LFDp9KAR8rhNK1dImw/ccOXMkP6vLVyDnsvnIGFM7iQ+nc5uHNLE1naY\niylIeNYUGj7WT0VFj8hm0Ag176Xi15ABP2xjprZvDMXvUou1nvXbYn+6IdcKRoJ4\nIpUjtrKDlzRPs7yk9lOXXRsv0ljUeiiQdZdx2QVSpuR6ItuQnQT1FfptSqkgXQcG\nVjMVIiHGENQnFc+NSa38azf8kz/zeKiPnNhSn13LNMdvDmb8xbO4BBGdYc2fVKwE\n8DqaZAQMglOSIsP4cEJY8qovOZzmrxhVgC+mjQIDAQABAoIBAA8QoSC0xydAHbg/\nuA9IWabdEp22EIXFdU+9KPZ4zF1FWxSHFBAz706Kk5dZnvshFRMzd50xX0KhEF1d\nYSvGVu839boiD0ICYDdTXHdwyF8xfJ1b0pRD7glMXyiZOsgFdtNli18Dq0sVh8Gr\ne05mO9TAJ1NDnlZz121fwjzC2JPxMwV4i90i3TqNUTS1nxm5Hm139lDgPg3WlbgV\nJzWaw5csIkcLIAGiK87XtLcMTu3CWfnygY8z7s2FsxkYkGetCnHfyEmEpb03trbu\n9uuz9HxirJqOS3nqOLho4u8Cwps3+yqxrYLM2G94o4cQsrbGc7meGEqqDZ2xVArr\nWJj4BUkCgYEA6dF7lkhD9IKMeFSXg/ik1h93yJsKFiEso/4O8A0D1zL4Pxn3KQLe\nwwrAUvgE4PvYMQSTJ397NwOuEvg6GHN3kYZKPgvQQD17mWxNs/iqsMo7Za7va1Ym\nTe7umD0Oq6oPnKVLRt1PWRjN8+gK2bMqYSGfzzcwNQgqkLPy0W8XM88CgYEAy5LX\nkjlB7qEUN7WallhAAjQtGgXrvYJH4kEk8SxpHvFF/eUuizsS0GpGxp/i8JVV0Sas\n+dnUBcZMVF8aOdHPWQ4zt8DXt53qux0l1T7L8p4eM+cXEqeuxB4kIZ1GjewSKw2j\nQ3+qZmajxqiLKm6UXDJ9CMeb53/jc5ITgh+HauMCgYAO3A5TpbIT5vwQZaffbjzj\nksplCF1ivKb+oRXH8bvNwGKAeCD6DUGk+ZjxbOu6dKbvro+/kd19yJEWiYn/pc7y\ng6tSOCP7AS1KudRSXLpUU/XkZ3K1yprSlx24tSCqjjtBxEt9bHEvg2ELYDLYVQeb\ndqyWWbaJmEREP/ttjfbWhwKBgQCvdxooBwI1VNHAUt+zxs0lGSPm0kOnTKv48H2P\nAuB4sy3I8cl0aK6GxZPLj/RjudQGOnfNw1tkvs77yh0oyRcXg45ATA+jTJIORcle\nTIotzOvrgLv6cF3K3M/3yUAPA/OE+HRIsbmGGeIAUTXilP17mmj7MFHI8Ap0iuwV\ntGdcUQKBgFYehJfnoM5jcwx8HERqf/fXKZj5HWBkeyepj8kGOqVQbq1wVekREp7I\n/eLFy+RlT2VPx5zmzbarj9GcJanv0J3JSBCG3JLocCzmcqfr6ov3wQzKVWuVWd9Y\n6iyormf+N45Hv6RTRV068sYbOZP/+JMFpNJ52N4vtXrZ30JcB6X7\n-----END RSA PRIVATE KEY-----"
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LANG=zh_CN.UTF-8 \
    LC_ALL=C \
    SHELL=/bin/bash \
    JD_DIR=/jd \
    QL_DIR=/ql \
    DEBIAN_FRONTEND=noninteractive \
    PS1="\u@\h:\w \$ "
SHELL ["/bin/bash", "-c"]
RUN source ~/.bashrc \
    && apt-get update \
    && apt-get install -y bash \
                          build-essential \
                          apt-utils \
                          python3 \
                          python3-pip \
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
                          openssl \
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
                          openssl \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && pip --no-cache-dir install aiohttp requests wasmtime utils \
    && mkdir -p /root/.ssh \
    && echo -e ${kwjKEY} > /root/.ssh/id_rsa_kwj \
    && chmod 600 /root/.ssh/id_rsa_kwj \
    && echo -e "\tHost kwj\n\tHostname github.com\n\tIdentityFile=/root/.ssh/id_rsa_kwj" > /root/.ssh/config \
    && chmod 644 /root/.ssh/config \
    && npm config set strict-ssl false \
    && npm install -g websocketserver pm2 \
    && apt-get clean \
    && apt-get autoclean \ 
    && rm -rf /var/lib/apt/lists/*
WORKDIR /