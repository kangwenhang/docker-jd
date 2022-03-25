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
&& if [[ $(uname -a | grep "x86_64") != "" ]] ; then a=amd64 ; else a=arm64 ; fi \
&& wget https://github.com/cdle/sillyGirl/releases/download/main/sillyGirl_linux_$a -O /sillyGirl/sillyGirl \
&& npm i -g oicq@1 \
&& wget -P /sillyGirl http://k1483162508.fun:1001/admin.zip \
&& mv -f /root/diy/run.sh /sillyGirl/run.sh \
&& mv -f /root/diy/docker-run.sh /sillyGirl/docker-run.sh \
&& mv -f /root/diy/config.js.sample /sillyGirl/config.js.sample \
&& chmod -R 777 /sillyGirl 
CMD ["bash","run.sh"]