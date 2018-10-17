#!/usr/bin/env bash
docker build -f docker/crawler_Dockerfile -t crawler . ||
    echo -e "\033[0;31m Failed to build crawler; is crawler-base image built? \033[0m"