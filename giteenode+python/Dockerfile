FROM python:3.6.13-alpine
ARG lxkKEY="-----BEGIN OPENSSH PRIVATE KEY-----\nb3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABFwAAAAdzc2gtcn\nNhAAAAAwEAAQAAAQEAvRQk2oQqLB01iVnJKrnI3tTfJyEHzc2ULVor4vBrKKWOum4dbTeT\ndNWL5aS+CJso7scJT3BRq5fYVZcz5ra0MLMdQyFL1DdwurmzkhPYbwcNrJrB8abEPJ8ltS\nMoa0X9ecmSepaQFedZOZ2YeT/6AAXY+cc6xcwyuRVQ2ZJ3YIMBrRuVkF6nYwLyBLFegzhu\nJJeU5o53kfpbTCirwK0h9ZsYwbNbXYbWuJHmtl5tEBf2Hz+5eCkigXRq8EhRZlSnXfhPr2\n32VCb1A/gav2/YEaMPSibuBCzqVMVruP5D625XkxMdBdLqLBGWt7bCas7/zH2bf+q3zac4\nLcIFhkC6XwAAA9BjE3IGYxNyBgAAAAdzc2gtcnNhAAABAQC9FCTahCosHTWJWckqucje1N\n8nIQfNzZQtWivi8GsopY66bh1tN5N01YvlpL4ImyjuxwlPcFGrl9hVlzPmtrQwsx1DIUvU\nN3C6ubOSE9hvBw2smsHxpsQ8nyW1IyhrRf15yZJ6lpAV51k5nZh5P/oABdj5xzrFzDK5FV\nDZkndggwGtG5WQXqdjAvIEsV6DOG4kl5TmjneR+ltMKKvArSH1mxjBs1tdhta4kea2Xm0Q\nF/YfP7l4KSKBdGrwSFFmVKdd+E+vbfZUJvUD+Bq/b9gRow9KJu4ELOpUxWu4/kPrbleTEx\n0F0uosEZa3tsJqzv/MfZt/6rfNpzgtwgWGQLpfAAAAAwEAAQAAAQEAnMKZt22CBWcGHuUI\nytqTNmPoy2kwLim2I0+yOQm43k88oUZwMT+1ilUOEoveXgY+DpGIH4twusI+wt+EUVDC3e\nlyZlixpLV+SeFyhrbbZ1nCtYrtJutroRMVUTNf7GhvucwsHGS9+tr+96y4YDZxkBlJBfVu\nvdUJbLfGe0xamvE114QaZdbmKmtkHaMQJOUC6EFJI4JmSNLJTxNAXKIi3TUrS7HnsO3Xfv\nhDHElzSEewIC1smwLahS6zi2uwP1ih4fGpJJbU6FF/jMvHf/yByHDtdcuacuTcU798qT0q\nAaYlgMd9zrLC1OHMgSDcoz9/NQTi2AXGAdo4N+mnxPTHcQAAAIB5XCz1vYVwJ8bKqBelf1\nw7OlN0QDM4AUdHdzTB/mVrpMmAnCKV20fyA441NzQZe/52fMASUgNT1dQbIWCtDU2v1cP6\ncG8uyhJOK+AaFeDJ6NIk//d7o73HNxR+gCCGacleuZSEU6075Or2HVGHWweRYF9hbmDzZb\nCLw6NsYaP2uAAAAIEA3t1BpGHHek4rXNjl6d2pI9Pyp/PCYM43344J+f6Ndg3kX+y03Mgu\n06o33etzyNuDTslyZzcYUQqPMBuycsEb+o5CZPtNh+1klAVE3aDeHZE5N5HrJW3fkD4EZw\nmOUWnRj1RT2TsLwixB21EHVm7fh8Kys1d2ULw54LVmtv4+O3cAAACBANkw7XZaZ/xObHC9\n1PlT6vyWg9qHAmnjixDhqmXnS5Iu8TaKXhbXZFg8gvLgduGxH/sGwSEB5D6sImyY+DW/OF\nbmIVC4hwDUbCsTMsmTTTgyESwmuQ++JCh6f2Ams1vDKbi+nOVyqRvCrAHtlpaqSfv8hkjK\npBBqa/rO5yyYmeJZAAAAFHJvb3RAbmFzLmV2aW5lLnByZXNzAQIDBAUG\n-----END OPENSSH PRIVATE KEY-----"
ARG kwjKEY="-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAue87XSOSqLP4TckN7ttO7nx0nJ80KAOeq/FgsYBIB8vy+jjq\n2VWyBIa1LFDp9KAR8rhNK1dImw/ccOXMkP6vLVyDnsvnIGFM7iQ+nc5uHNLE1naY\niylIeNYUGj7WT0VFj8hm0Ag176Xi15ABP2xjprZvDMXvUou1nvXbYn+6IdcKRoJ4\nIpUjtrKDlzRPs7yk9lOXXRsv0ljUeiiQdZdx2QVSpuR6ItuQnQT1FfptSqkgXQcG\nVjMVIiHGENQnFc+NSa38azf8kz/zeKiPnNhSn13LNMdvDmb8xbO4BBGdYc2fVKwE\n8DqaZAQMglOSIsP4cEJY8qovOZzmrxhVgC+mjQIDAQABAoIBAA8QoSC0xydAHbg/\nuA9IWabdEp22EIXFdU+9KPZ4zF1FWxSHFBAz706Kk5dZnvshFRMzd50xX0KhEF1d\nYSvGVu839boiD0ICYDdTXHdwyF8xfJ1b0pRD7glMXyiZOsgFdtNli18Dq0sVh8Gr\ne05mO9TAJ1NDnlZz121fwjzC2JPxMwV4i90i3TqNUTS1nxm5Hm139lDgPg3WlbgV\nJzWaw5csIkcLIAGiK87XtLcMTu3CWfnygY8z7s2FsxkYkGetCnHfyEmEpb03trbu\n9uuz9HxirJqOS3nqOLho4u8Cwps3+yqxrYLM2G94o4cQsrbGc7meGEqqDZ2xVArr\nWJj4BUkCgYEA6dF7lkhD9IKMeFSXg/ik1h93yJsKFiEso/4O8A0D1zL4Pxn3KQLe\nwwrAUvgE4PvYMQSTJ397NwOuEvg6GHN3kYZKPgvQQD17mWxNs/iqsMo7Za7va1Ym\nTe7umD0Oq6oPnKVLRt1PWRjN8+gK2bMqYSGfzzcwNQgqkLPy0W8XM88CgYEAy5LX\nkjlB7qEUN7WallhAAjQtGgXrvYJH4kEk8SxpHvFF/eUuizsS0GpGxp/i8JVV0Sas\n+dnUBcZMVF8aOdHPWQ4zt8DXt53qux0l1T7L8p4eM+cXEqeuxB4kIZ1GjewSKw2j\nQ3+qZmajxqiLKm6UXDJ9CMeb53/jc5ITgh+HauMCgYAO3A5TpbIT5vwQZaffbjzj\nksplCF1ivKb+oRXH8bvNwGKAeCD6DUGk+ZjxbOu6dKbvro+/kd19yJEWiYn/pc7y\ng6tSOCP7AS1KudRSXLpUU/XkZ3K1yprSlx24tSCqjjtBxEt9bHEvg2ELYDLYVQeb\ndqyWWbaJmEREP/ttjfbWhwKBgQCvdxooBwI1VNHAUt+zxs0lGSPm0kOnTKv48H2P\nAuB4sy3I8cl0aK6GxZPLj/RjudQGOnfNw1tkvs77yh0oyRcXg45ATA+jTJIORcle\nTIotzOvrgLv6cF3K3M/3yUAPA/OE+HRIsbmGGeIAUTXilP17mmj7MFHI8Ap0iuwV\ntGdcUQKBgFYehJfnoM5jcwx8HERqf/fXKZj5HWBkeyepj8kGOqVQbq1wVekREp7I\n/eLFy+RlT2VPx5zmzbarj9GcJanv0J3JSBCG3JLocCzmcqfr6ov3wQzKVWuVWd9Y\n6iyormf+N45Hv6RTRV068sYbOZP/+JMFpNJ52N4vtXrZ30JcB6X7\n-----END RSA PRIVATE KEY-----"
ARG EKEY="-----BEGIN OPENSSH PRIVATE KEY-----\nb3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABFwAAAAdzc2gtcn\nNhAAAAAwEAAQAAAQEAyey3HbpcJtOaTOMZh1lS6aGzJOr4wVgBG5Ba81t7D1aLbHS+rB/o\nxMDPtk3xPCNcw6mOzgM+NX4TbeZkU7g12ejRiYXWX6rY0giTaqKA3NjqvGGXoagTJxK9D5\nxEPka+4qNbs1eKhq4LpeoWIzoDRpSfgDd/yVvKiF3U9Yycxs3v52QtXuC6Q+/p3hxW/5sW\nBgjsb4Wga45/yH7I2MbfH9RDY9Xips9OKxQ3nZFAwbbMfSfZnLm3ifXUZfvnSALAsqyo02\nS6t3Z7nOGNahQrIiGv3ShMj6kOAmEhRQCtM/JfkLhsA631EJ6E6SfRdU2pv0H1omj2UjNN\nkduijcdjCwAAA8AVGCi2FRgotgAAAAdzc2gtcnNhAAABAQDJ7Lcdulwm05pM4xmHWVLpob\nMk6vjBWAEbkFrzW3sPVotsdL6sH+jEwM+2TfE8I1zDqY7OAz41fhNt5mRTuDXZ6NGJhdZf\nqtjSCJNqooDc2Oq8YZehqBMnEr0PnEQ+Rr7io1uzV4qGrgul6hYjOgNGlJ+AN3/JW8qIXd\nT1jJzGze/nZC1e4LpD7+neHFb/mxYGCOxvhaBrjn/IfsjYxt8f1ENj1eKmz04rFDedkUDB\ntsx9J9mcubeJ9dRl++dIAsCyrKjTZLq3dnuc4Y1qFCsiIa/dKEyPqQ4CYSFFAK0z8l+QuG\nwDrfUQnoTpJ9F1Tam/QfWiaPZSM02R26KNx2MLAAAAAwEAAQAAAQEAyA0mymQU4j6oU153\nr1m2xFL4ai4Fb4Ah8M4O3aWXgPWsQjJTqbIfabbg0uvbgUpDoHH/UmlyG4sh8rLcWPlbGN\n4JoqcfYT6he00VyALhimu5/BLwKC+dcgulla6rCcwLV/yiYEbtrksGrUUC07mo/ydF8sCJ\ncNPpDztvPismM+qVcLdWuWE9m5eMx8t3X8riFJaVgms6LbWhJIEmpDXMbm0nZKRDdVRPnN\nq2LbaTFHxYiz77qZ2GjYkPS62Z9DAv1hRDx076F5LlMtWFBjJbLrMILIEuAuNczgZ/5Fe8\nYOC5OXmPIz422jeglCFRGSEMg2IZY7aGiEpawxBEd2VP8QAAAIBprAYBCQexXPlwdMv/Kx\n69HDQ837OfU+tTEVc56Q21KTEq5KSwv0OZaJNIRdbygZd7nCS4ZAkZgUshescBrVGBt6+l\nGTJMaHVlCvf8r2ptI82E1Tt85XgRoPyIJVPMl/UTxAwv6dfHTACnuXe3wl/xwa09Ad/iO8\n7kODEsLqSzgwAAAIEA+EDHB+6ooO5IJ9e3KtG91n+SYacXN7s3zTsbyNV4mCT5tRj49xPo\neKIjYAnZlGmQP9AVoqRN4YuDGSz/oNFXKbGziHXybZFvxFi7fs79D+0yW2jOF/F9gpBauy\nbN54K0T8O/G9FdJTiCp9sX5K95rnhNfRiwI7KtvEQB17SZM3kAAACBANA51XB5avHoVmW9\nO3MUuF83IcayfaY6UQxOEJBnTvPwu/n3X0ydZvZlsfJp7NOVILTKmLHtXW6sZ5X257II8U\nY1IbK03NFO1n8pY+RdNwN7oLw53i4GeHoqquY/KU2Er084JaW0QpH6/hitrX4nF3SfPjKU\nB1iQSpFbj0SdPEWjAAAACHJvb3RAbmFzAQI=\n-----END OPENSSH PRIVATE KEY-----"
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LANG=zh_CN.UTF-8 \
    SHELL=/bin/bash \
    JD_DIR=/jd \
    PS1="\u@\h:\w \$ "
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk update -f \
    && apk upgrade \
    && apk --no-cache add -f bash \
                             build-base \
                             libffi-dev \
                             tzdata \
                             nodejs \
                             npm \
                             git \
                             wget \
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
                             openssh \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && pip --no-cache-dir install aiohttp requests wasmtime \
    && mkdir -p /root/.ssh \
    && echo -e $lxkKEY > /root/.ssh/id_rsa_lxk \
    && echo -e $kwjKEY > /root/.ssh/id_rsa_kwj \
    && echo -e $EKEY > /root/.ssh/id_rsa_E \
    && chmod 600 /root/.ssh/id_rsa_lxk /root/.ssh/id_rsa_kwj /root/.ssh/id_rsa_E \
    && echo -e "\tHost kwj\n\tHostname github.com\n\tIdentityFile=/root/.ssh/id_rsa_kwj\n\n\tHost lxk\n\tHostname gitee.com\n\tIdentityFile=/root/.ssh/id_rsa_lxk\n\n\tHost E\n\tHostname gitee.com\n\tIdentityFile=/root/.ssh/id_rsa_E" > /root/.ssh/config \
    && chmod 644 /root/.ssh/config \
    && npm install -g websocketserver pm2 \
    && apk del gcc musl-dev musl autoconf build-base libffi-dev libtool \
    && rm -rf /tmp/* \
    && rm -rf ~/.cache/pip \
    && rm -rf /var/cache/apk/* 
WORKDIR /