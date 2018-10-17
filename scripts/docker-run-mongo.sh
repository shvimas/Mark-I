#!/usr/bin/env bash
docker run \
    -d \
    --name crawler-mongo \
    --network crawler-network \
    -p 27017:27017 \
    --env-file envs/mongo-env.list \
    crawler-mongo:latest