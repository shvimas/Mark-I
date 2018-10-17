#!/usr/bin/env bash
docker run -d --name=crawler --network crawler-network --env-file envs/crawler-env.list crawler ||
    echo -e "\033[0;31m Failed to start crawler; maybe MongoDB container is not up? \033[0m"