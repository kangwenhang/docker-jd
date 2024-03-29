FROM ubuntu:22.10
ARG PUSH_URL=https://github.com/kangwenhang/docker.git
ARG PUSH_BRANCH=master
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LANG=zh_CN.UTF-8 \
    LC_ALL=C \
    SHELL=/bin/bash \
    DEBIAN_FRONTEND=noninteractive \
    PS1="\u@\h:\w \$ " \
    dir_root=/push
SHELL ["/bin/bash", "-c"]
WORKDIR ${dir_root}
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
    && apt-get upgrade \
    && apt-get update \
    && apt-get install -y bash \
                          git \
                          curl \
                          wget \
                          cron \
                          tzdata \
                          tar \
                          jq \
                          vim \
                          busybox \
                          rsyslog \
                          sudo \
                          postfix \
                          rename \
                          rsync \
                          nodejs \
                          npm \
    && apt-get clean \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* \
    && npm config set strict-ssl false \
    && npm install -g pm2 \
    && sed -i 's/$PrivDrop/# $PrivDrop/g' /etc/rsyslog.conf \
    && sed -i '/imklog/s/^/#/' /etc/rsyslog.conf \
    && sed -i 's/#cron/cron/g' /etc/rsyslog.d/50-default.conf \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && ln -sf /bin/bash /bin/sh \
    && git clone -b ${PUSH_BRANCH} ${PUSH_URL} ${dir_root}/repo/docker \
    && cp -rf ${dir_root}/repo/docker/* ${dir_root} \
    && chmod -R 777 ${dir_root}
ENTRYPOINT ["./docker/docker-entrypoint.sh"]
