#!/usr/bin/env bash
docker run --name mongo -d --network crawler-network -p 27017:27017 --env-file envs/mongo-env.list mongo:4.0.3