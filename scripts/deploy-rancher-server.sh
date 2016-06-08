#!/bin/bash

# Use docker machine to deploy the rancher server directly on Exoscale
docker-machine create --driver exoscale \
    --exoscale-api-key $DEMO_API_KEY \
    --exoscale-api-secret-key $DEMO_SECRET_KEY \
    --exoscale-instance-profile 'Tiny' \
    --exoscale-image 'ubuntu-16.04' \
    --exoscale-security-group 'demo-devoxx' \
    --exoscale-availability-zone 'ch-dk-2' \
    "devoxx-uk"

eval $(docker-machine env devoxx-uk)

# Using 1.1.0-dev3 for now until latest or stable are good enough
docker run -d -p 8080:8080 rancher/server:v1.1.0-dev3
