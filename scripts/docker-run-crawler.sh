#!/usr/bin/env bash
docker run -dit --name=bit-crawler -v ~/BitCrawler/logs:/crawler/logs bit-crawler