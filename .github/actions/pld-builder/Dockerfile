FROM ubuntu:21.04

RUN apt-get update && apt-get install -y \
    pandoc \
    make \
    wget \
    python3 \
    python3-yaml \
    && rm -rf /var/lib/apt/lists/*

# Install tectonic
RUN cd /tmp && \
    wget https://github.com/tectonic-typesetting/tectonic/releases/download/tectonic%400.8.0/tectonic-0.8.0-x86_64-unknown-linux-musl.tar.gz \
    && tar -xf tectonic-0.7.1-x86_64-unknown-linux-musl.tar.gz \
    && mv tectonic /usr/local/bin \
    && rm tectonic-0.7.1-x86_64-unknown-linux-musl.tar.gz

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
