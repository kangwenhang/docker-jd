FROM k1483162508/base:ndbase
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LANG=zh_CN.UTF-8 \
    LC_ALL=C \
    SHELL=/bin/bash \
    PS1="\u@\h:\w \$ " 
COPY /sillyGirl/diy/ /root/diy/
WORKDIR /sillyGirl
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& echo "Asia/Shanghai" > /etc/timezone \
&& mkdir -p /sillyGirl/plugin/web/admin \
&& mkdir -p /etc/sillyGirl \
&& if [[ $(uname -a | grep "x86_64") != "" ]] ; then a=amd64 ; else a=arm64 ; fi \
&& wget https://github.com/cdle/sillyGirl/releases/download/main/sillyGirl_linux_$a -O /sillyGirl/sillyGirl  \
&& wget -P /sillyGirl http://k1483162508.fun:1001/admin.zip \
&& mv -f /root/diy/sets.conf.sample /sillyGirl/sets.conf.sample \
&& mv -f /root/diy/run.sh /sillyGirl/run.sh \
&& chmod -R 777 /sillyGirl 
CMD ["sh","run.sh"]