FROM ubuntu:24.04
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LANG=zh_CN.UTF-8 \
    LC_ALL=C \
    SHELL=/bin/bash \
    DEBIAN_FRONTEND=noninteractive \
    PS1="\u@\h:\w \$ " \
    dir_root=/photos
SHELL ["/bin/bash", "-c"]
WORKDIR ${dir_root}
COPY docker/docker-entrypoint.sh ${dir_root}/docker-entrypoint.sh
COPY script /photos/script
COPY sample /photos/sample
RUN apt-get upgrade \
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
                          python3 \
                          pip \
    && python3 --version \
    && apt-get clean \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* \
    && npm config set strict-ssl false \
    && npm install -g pm2 \
    && mv /usr/lib/python3.x/EXTERNALLY-MANAGED /usr/lib/python3.x/EXTERNALLY-MANAGED.bk \
    && pip install setuptools Pillow configparser pyexiftool \
    && sed -i 's/$PrivDrop/# $PrivDrop/g' /etc/rsyslog.conf \
    && sed -i '/imklog/s/^/#/' /etc/rsyslog.conf \
    && sed -i 's/#cron/cron/g' /etc/rsyslog.d/50-default.conf \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && ln -sf /bin/bash /bin/sh \
    && chmod +x ${dir_root}/docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
