#!/bin/bash
# Sends a GET request to a URL and displays the body of the response with a custom header

if [ "$#" -ne 1 ]; then
	echo "Usage: $0 URL"
	exit 1
fi
url=$1
curl -s H "X-School-User-Id: 98" "$url"
