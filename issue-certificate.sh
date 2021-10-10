#!/bin/bash

CB=`docker ps --format='{{.Names}}' --filter=label=meta.role=certbot`

EMAIL=$2

CERTNAME=$1
DOMAIN=$1

docker exec $CB certbot certonly --non-interactive --standalone --email $2 --agree-tos --keep --preferred-challenges http --cert-name "$CERTNAME" -d "$DOMAIN"

cat "./data/certbot/etc/live/$CERTNAME/privkey.pem" "./data/certbot/etc/live/$CERTNAME/fullchain.pem" > "./data/certificates/$CERTNAME.pem"

