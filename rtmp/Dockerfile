FROM tiangolo/nginx-rtmp

COPY nginx.conf /etc/nginx/nginx.conf
COPY mime.types /etc/nginx/mime.types

COPY index.html /www/
COPY network.m3u8 /www/
COPY network0.ts /www/
COPY network1.ts /www/

EXPOSE 8080
