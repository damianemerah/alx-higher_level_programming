#!/usr/bin/python3
"""Display the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
