#!/bin/bash
#send a JSON POST request to a url and displays the body of the response
curl -sX POST "$1" -H "Content-Type: application/json" -d "@$2"
