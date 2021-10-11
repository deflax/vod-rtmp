FROM buildpack-deps:stretch

# Versions of modules to use
ENV NGINX_VERSION nginx-1.18.0
ENV NGINX_RTMP_MODULE_VERSION 1.2.1
ENV NGINX_HTTP_FLV_MODULE_VERSION 1.2.9

# Install dependencies
RUN apt-get update && \
    apt-get install -y ca-certificates openssl libssl-dev && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Download and decompress Nginx
RUN mkdir -p /tmp/build/nginx && \
    cd /tmp/build/nginx && \
    wget -O ${NGINX_VERSION}.tar.gz https://nginx.org/download/${NGINX_VERSION}.tar.gz && \
    tar -zxf ${NGINX_VERSION}.tar.gz

# Download and decompress RTMP module
RUN mkdir -p /tmp/build/nginx-rtmp-module && \
    cd /tmp/build/nginx-rtmp-module && \
    wget -O nginx-rtmp-module-${NGINX_RTMP_MODULE_VERSION}.tar.gz https://github.com/arut/nginx-rtmp-module/archive/v${NGINX_RTMP_MODULE_VERSION}.tar.gz && \
    tar -zxf nginx-rtmp-module-${NGINX_RTMP_MODULE_VERSION}.tar.gz && \
    cd nginx-rtmp-module-${NGINX_RTMP_MODULE_VERSION}

# Download and decompress HTTP FLV module
RUN mkdir -p /tmp/build/nginx-http-flv-module && \
    cd /tmp/build/nginx-http-flv-module && \
    wget -O nginx-http-flv-module-${NGINX_HTTP_FLV_MODULE_VERSION}.tar.gz https://github.com/winshining/nginx-http-flv-module/archive/v${NGINX_HTTP_FLV_MODULE_VERSION}.tar.gz && \
    tar -zxf nginx-http-flv-module-${NGINX_HTTP_FLV_MODULE_VERSION}.tar.gz && \
    cd nginx-http-flv-module-${NGINX_HTTP_FLV_MODULE_VERSION}

# Build and install Nginx
# The default puts everything under /usr/local/nginx, so it's needed to change
# it explicitly. Not just for order but to have it in the PATH
RUN cd /tmp/build/nginx/${NGINX_VERSION} && \
    ./configure \
        --sbin-path=/usr/local/sbin/nginx \
        --conf-path=/etc/nginx/nginx.conf \
        --error-log-path=/var/log/nginx/error.log \
        --pid-path=/var/run/nginx/nginx.pid \
        --lock-path=/var/lock/nginx/nginx.lock \
        --http-log-path=/var/log/nginx/access.log \
        --http-client-body-temp-path=/tmp/nginx-client-body \
        --with-http_ssl_module \
        --with-threads \
        --with-ipv6 \
        #--add-module=/tmp/build/nginx-http-flv-module/nginx-http-flv-module-${NGINX_HTTP_FLV_MODULE_VERSION} && \
        --add-module=/tmp/build/nginx-rtmp-module/nginx-rtmp-module-${NGINX_RTMP_MODULE_VERSION} && \
    make -j $(getconf _NPROCESSORS_ONLN) && \
    make install && \
    mkdir /var/lock/nginx && \
    rm -rf /tmp/build

# Forward logs to Docker
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

# Set up config file
COPY nginx.conf /etc/nginx/nginx.conf
COPY mime.types /etc/nginx/mime.types

# Copy fallback data
COPY network.m3u8 /www/fallback/
COPY network0.ts /www/fallback/
COPY network1.ts /www/fallback/

EXPOSE 1935
EXPOSE 8080
EXPOSE 18080
CMD ["nginx", "-g", "daemon off;"]

