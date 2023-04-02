#!/bin/bash
#Deletes url
response=(curl -sX DELECT $1)
echo "I'm a DELETE request"
