#!/usr/bin/env bash
git pull && docker build -f docker/alpine_Dockerfile -t alpine-bit-crawler .