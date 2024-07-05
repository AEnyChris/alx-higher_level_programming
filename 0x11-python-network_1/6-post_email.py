#!/usr/bin/python3
"""This module makes a request to a given url
using the requests module
"""

if __name__ == "__main__":
    import requests
    import sys

    payload = {'email': sys.argv[2]}

    resp = requests.post(sys.argv[1], data=payload)

    print(resp.text)
