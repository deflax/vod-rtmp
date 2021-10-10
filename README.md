# vod-rtmp

## How to run

1. `apt install docker.io docker-compose`
2. `docker-compose build`
3. `./gen-selfsigned.sh`
4. `docker-compose up`
5. `./issue-certificate.sh example.com info@example.com`

6. Encoder server = `rtmp://example:1935/live` key = `live?key=supersecret`
7. Open a browser and go to `https://example.com` to view your live stream via hls.js
