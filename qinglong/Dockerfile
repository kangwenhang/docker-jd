FROM k1483162508/base:2
LABEL maintainer="whyour"
ARG JD_BASE_URL=https://github.com.cnpmjs.org/whyour/qinglong
ARG JD_BASE_BRANCH=master
ARG JD_SCRIPTS_URL=https://github.com.cnpmjs.org/RikudouPatrickstar/jd_scripts
ARG JD_SCRIPTS_BRANCH=master
ENV JD_DIR=/jd
RUN touch ~/.bashrc \
    && mkdir /run/nginx \
    && git clone -b ${JD_BASE_BRANCH} ${JD_BASE_URL} ${JD_DIR} \
    && cd ${JD_DIR} \
    && cp -f .env.example .env \
    && ln -sf ${JD_DIR}/shell/jd.sh /usr/local/bin/jd \
    && ln -sf ${JD_DIR}/shell/git_pull.sh /usr/local/bin/git_pull \
    && ln -sf ${JD_DIR}/shell/rm_log.sh /usr/local/bin/rm_log \
    && ln -sf ${JD_DIR}/shell/export_sharecodes.sh /usr/local/bin/export_sharecodes \
    && ln -sf ${JD_DIR}/shell/git_diy.sh /usr/local/bin/diy \
    && ln -sf ${JD_DIR}/shell/notify.sh /usr/local/bin/notify \
    && npm install \
    && npm build \
    && npm build-back \
    && npm install --production \
    && git clone -b ${JD_SCRIPTS_BRANCH} ${JD_SCRIPTS_URL} ${JD_DIR}/scripts \
    && cd ${JD_DIR}/scripts \
    && npm install --production\
    && npm install -g pm2 \
    && rm -rf /root/.npm
WORKDIR ${JD_DIR}
ENTRYPOINT bash ${JD_DIR}/docker/docker-entrypoint.sh