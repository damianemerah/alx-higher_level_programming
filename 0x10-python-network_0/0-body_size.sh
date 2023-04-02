#!/bin/bash

# Get the URL from the command line argument
url=$1

# Send a request to the URL using curl
echo $(curl -s -o /dev/null -w "%{size_download}" "$url")
