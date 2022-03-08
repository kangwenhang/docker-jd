FROM k1483162508/base:ndbase
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LANG=zh_CN.UTF-8 \
    LC_ALL=C \
    SHELL=/bin/bash \
    PS1="\u@\h:\w \$ " \
    DEBIAN_FRONTEND=noninteractive \
    RUN_AS_ROOT=true
SHELL ["/bin/bash", "-c"]
COPY /sillyGirl/diy/ /root/diy/
RUN source ~/.bashrc \
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& echo "Asia/Shanghai" > /etc/timezone \
&& mkdir -p /sillyGirl \
&& if [[ $(uname -a | grep "x86_64") != "" ]] ; then a=amd64 ; else a=arm64 fi \
&& wget https://github.com/cdle/sillyGirl/releases/download/main/sillyGirl_linux_$a -O /sillyGirl \
&& mv -f /root/diy/sets.conf.sample /sillyGirl/sets.conf.sample \
&& mv -f /root/diy/run.sh /sillyGirl/run.sh \
&& chmod 777 sillyGirl 
WORKDIR /sillyGirl
CMD ["sh","run.sh"]