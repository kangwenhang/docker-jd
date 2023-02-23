FROM k1483162508/base:tgbase
ARG DIY_URL="https://github.com/kangwenhang/diy.git" \
    DIY_BRANCH="PagerMaid-Pyro"
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LANG=zh_CN.UTF-8 \
    LC_ALL=C \
    SHELL=/bin/bash \
    PS1="\u@\h:\w \$ " \
    DEBIAN_FRONTEND=noninteractive \
    RUN_AS_ROOT=true
SHELL ["/bin/bash", "-c"]
WORKDIR /pagermaid/workdir
RUN source ~/.bashrc \
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& echo "Asia/Shanghai" > /etc/timezone \
&& sed -e 's;^# \(%wheel.*NOPASSWD.*\);\1;g' -i /etc/sudoers \
&& mkdir -p /pagermaid/workdir/ \
&& git clone -b master https://github.com/TeamPGM/PagerMaid-Pyro.git /pagermaid/workdir \
&& git config --global pull.ff only \
&& mkdir -p /pagermaid/workdir/config/ \
&& mkdir -p /pagermaid/workdir/data/ \
&& cd /pagermaid/workdir/utils \
&& git clone -b ${DIY_BRANCH} ${DIY_URL} diy \
&& ln -sf /pagermaid/workdir/utils/diy/update.sh /pagermaid/workdir/update.sh \
&& cd /pagermaid/workdir \
&& pip install --upgrade pip \
&& pip3 install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
CMD ["bash","/pagermaid/workdir/utils/diy/run.sh"]