FROM k1483162508/base:tgbase
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
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& echo "Asia/Shanghai" > /etc/timezone \
&& sed -e 's;^# \(%wheel.*NOPASSWD.*\);\1;g' -i /etc/sudoers \
&& mkdir -p /pagermaid/workdir \
&& git clone -b master https://gitlab.com/Xtao-Labs/pagermaid-modify.git /pagermaid/workdir \
&& git config --global pull.ff only \
&& mv -f /root/diy/docker-run.sh /pagermaid/workdir/utils/docker-run.sh \
&& cd /pagermaid/workdir \
&& pip3 install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
ENTRYPOINT ["/init"]