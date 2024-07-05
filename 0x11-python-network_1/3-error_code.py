#!/usr/bin/python3
"""This module makes a request to a given url"""

if __name__ == "__main__":
    import urllib.request as request
    from urllib.error import HTTPError
    import sys

    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as resp:
            page = resp.read()
        print(page.decode())
    except HTTPError as e:
        print(f"Error code: {e.code}")
