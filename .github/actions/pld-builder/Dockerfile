FROM ubuntu:21.04
LABEL org.opencontainers.image.source="https://github.com/PizziPayment/PizziPLD"

VOLUME /source
WORKDIR /source

RUN apt-get update && apt-get install -y \
    pandoc \
    make \
    wget \
    python3 \
    python3-yaml \
    && rm -rf /var/lib/apt/lists/*

# Install tectonic
RUN cd /tmp && \
    TECTONIC_ARCHIVE='tectonic-0.8.0-x86_64-unknown-linux-musl.tar.gz'; \
    TECTONIC_URL='https://github.com/tectonic-typesetting/tectonic/releases/download/tectonic%400.8.0/tectonic-0.8.0-x86_64-unknown-linux-musl.tar.gz'; \
    wget $TECTONIC_URL \
    && tar -xf $TECTONIC_ARCHIVE \
    && mv tectonic /usr/local/bin \
    && rm $TECTONIC_ARCHIVE

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
