FROM k1483162508/base:tgbase
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LANG=zh_CN.UTF-8 \
    LC_ALL=C \
    SHELL=/bin/bash \
    PS1="\u@\h:\w \$ " \
    DEBIAN_FRONTEND=noninteractive \
    RUN_AS_ROOT=true
SHELL ["/bin/bash", "-c"]
COPY /PagerMaid-Pyro/diy/ /root/diy/
RUN source ~/.bashrc \
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& echo "Asia/Shanghai" > /etc/timezone \
&& sed -e 's;^# \(%wheel.*NOPASSWD.*\);\1;g' -i /etc/sudoers \
&& mkdir -p /pagermaid/workdir/ \
&& git clone -b master https://github.com/TeamPGM/PagerMaid-Pyro.git /pagermaid/workdir \
&& git config --global pull.ff only \
&& mkdir -p /pagermaid/workdir/config/ \
&& mkdir -p /pagermaid/workdir/data/ \
&& mv -f /root/diy/docker-run.sh /pagermaid/workdir/utils/docker-run.sh \
&& mv -f /root/diy/run.sh /pagermaid/workdir/run.sh \
&& rm -rf /root/diy \
&& cd /pagermaid/workdir \
&& pip3 install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
WORKDIR /pagermaid/workdir
CMD ["bash","run.sh"]