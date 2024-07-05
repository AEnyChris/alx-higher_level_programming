#!/usr/bin/python3
"""This module makes a request to a given url"""

if __name__ == "__main__":
    import urllib.request as request
    import sys

    with request.urlopen(sys.argv[1]) as resp:
        page = resp.info()
    print(page['X-Request-Id'])
