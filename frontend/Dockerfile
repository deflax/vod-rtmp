FROM python:3

RUN pip --no-cache-dir install \
    flask \
    pyyaml \
    uwsgi

RUN mkdir /code
COPY ./app /code

ADD https://github.com/bilibili/flv.js/releases/download/v1.5.0/flv.min.js /code/static/flv.min.js
RUN chmod 644 /code/static/flv.min.js

RUN mkdir -p /tmp/hls.js && \
    cd /tmp/hls.js && \
    wget -O hls.js.zip https://github.com/video-dev/hls.js/releases/download/v1.0.11/release.zip && \
    unzip hls.js.zip && \
    cp dist/hls.js /code/static/hls.js && \
    cp dist/hls.js.map /code/static/hls.js.map && \
    cp dist/hls.min.js /code/static/hls.min.js && \
    cp dist/hls.min.js.map /code/static/hls.min.js.map

RUN chmod 644 /code/static/hls.js
RUN chmod 644 /code/static/hls.js.map
RUN chmod 644 /code/static/hls.min.js
RUN chmod 644 /code/static/hls.min.js.map

USER nobody
WORKDIR /code
EXPOSE 5001
