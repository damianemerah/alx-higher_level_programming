#!/bin/bash
# Sends a GET request to a URL and displays the body of the response with a custom header

url=$1
curl -sH "X-School-User-Id: 98" "$url"
