# vod-rtmp

## How to run

1. `apt install docker.io docker-compose`
2. `cp docker-compose.yml.dist docker-compose.yml` and edit the env variables
3. `cd config/frontend && cp config.yml.dist config.yml` and edit the variables
4. `./gen-selfsigned.sh` - generate self signed haproxy cert for bootstraping
5. `docker-compose build`
8. `docker-compose up`
5. `./issue-certificate.sh example.com info@example.com` - issue LE production certificate
8. You can use the following command to rebuild and restart everything:
`docker-compose down ; docker-compose build; docker-compose up -d ; docker-compose logs --follow`

## Setup client
1. Encoder server = `rtmp://example:1935/live/` key = `stream?pass=supersecret`
2. Open a browser and go to `https://example.com` to view your live stream via flv.js

### Powered by
- https://github.com/tiangolo/nginx-rtmp-docker
- https://github.com/zom-bi/zomstream
- https://github.com/Abdisalan/blog-code-examples/tree/master/live-stream-part-3
