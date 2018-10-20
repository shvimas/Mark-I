#!/usr/bin/env bash
docker run -d --name=crawler --network crawler-network --env-file envs/crawler-env.list crawler