#!/bin/bash
# Send a request to the URL using curl
curl -s $1 | wc -c
