#!/usr/bin/python3
"""This module makes a request to a given url
using the requests module
"""

if __name__ == "__main__":
    import requests
    import sys

    resp = requests.get(sys.argv[1])

    print(resp.headers.get("X-Request-Id"))
