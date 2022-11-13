# syntax=docker/dockerfile:experimental
FROM debian:11
ENV LANG=en_US.UTF-8 \
    ENTRYPOINTD=${HOME}/entrypoint.d \
    USER=coder
RUN apt-get update \
  && apt-get install -y \
    curl \
    dumb-init \
    zsh \
    python3 \
    htop \
    locales \
    man \
    python3 \
    nano \
    npm \
    git \
    git-lfs \
    procps \
    openssh-client \
    sudo \
    vim.tiny \
    lsb-release \
  && git lfs install \
  && rm -rf /var/lib/apt/lists/* \
  && curl -v -L "https://github.com/coder/code-server/blob/main/ci/release-image/entrypoint.sh" -o /usr/bin/entrypoint.sh \
  && curl -v -L "https://github.com/coder/code-server/releases/download/v4.9.0-rc.1/code-server*.deb" -o /tmp/code-server*.deb \
  && ls /tmp/
  && npm i -g npm \
  && npm i -g pnpm \
  && sed -i "s/# en_US.UTF-8/en_US.UTF-8/" /etc/locale.gen \
  && locale-gen \
  && adduser --gecos '' --disabled-password coder \
  && echo "coder ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/nopasswd \
  && ARCH="$(dpkg --print-architecture)" \
  && curl -fsSL "https://github.com/boxboat/fixuid/releases/download/v0.5/fixuid-0.5-linux-$ARCH.tar.gz" | tar -C /usr/local/bin -xzf - \
  && chown root:root /usr/local/bin/fixuid \
  && chmod 4755 /usr/local/bin/fixuid \
  && mkdir -p /etc/fixuid \
  && printf "user: coder\ngroup: coder\n" > /etc/fixuid/config.yml \
  && --mount=from=packages,src=/tmp,dst=/tmp/packages dpkg -i /tmp/packages/code-server*$(dpkg --print-architecture).deb

EXPOSE 8080
USER 1000
WORKDIR /home/coder
ENTRYPOINT ["/usr/bin/entrypoint.sh", "--bind-addr", "0.0.0.0:8080", "."]
