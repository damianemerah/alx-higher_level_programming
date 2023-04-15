#!/bin/bash
#send a request to a url and display only the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
