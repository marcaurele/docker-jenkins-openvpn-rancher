#!/bin/bash

# Use docker machine to deploy the rancher server directly to Exoscale
docker-machine create --driver exoscale \
    --exoscale-api-key $DEMO_API_KEY \
    --exoscale-api-secret-key $DEMO_SECRET_KEY \
    --exoscale-instance-profile 'Tiny' \
    --exoscale-image 'ubuntu-16.04' \
    --exoscale-security-group 'demo-devoxx' \
    --exoscale-availability-zone 'ch-dk-2' \
    "devoxx-uk"

eval $(docker-machine env devoxx-uk)

docker run -d -p 8080:8080 rancher/server:latest