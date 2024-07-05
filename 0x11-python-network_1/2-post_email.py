#!/usr/bin/python3
"""This module makes a request to a given url"""

if __name__ == "__main__":
    import urllib.request as request
    import urllib.parse as parse
    import sys

    value = {'email': sys.argv[2]}
    email = parse.urlencode(value)
    email = email.encode('ascii')

    req = request.Request(sys.argv[1], data=email)
    with request.urlopen(req) as resp:
        page = resp.read()
    print(page.decode())
