#!/usr/bin/python3
"""Takes a url and email and sends POST request to the
url passed with email as parameter
Usage: ./2-post_email.py <URL> <email>
"""

import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(val).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
