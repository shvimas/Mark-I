#!/usr/bin/env bash
git pull && docker build -f docker/crawler_Dockerfile -t bit-crawler .