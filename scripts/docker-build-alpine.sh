#!/usr/bin/env bash
git pull && docker build -f docker/alpine_Dockerfile -t my-alpine-python3 .