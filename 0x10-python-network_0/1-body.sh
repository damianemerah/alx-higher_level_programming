#!/bin/bash

# Check if the user provided a URL as an argument
if [[ $# -eq 0 ]]; then
  echo "Usage: $0 <url>"
  exit 1
fi

# Send a GET request to the URL and display the body of the response if the status code is 200
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q "200" && curl -s "$1"

