#!/usr/bin/env bash
git pull && docker build -f docker/crawler_base_Dockerfile -t crawler-base .