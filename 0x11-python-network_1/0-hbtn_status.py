#!/usr/bin/python3
"""This module makes a request to a given url"""

if __name__ == "__main__":
    import urllib.request as request


    with request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        page = resp.read()

    print("Body response:")
    print(f"\t- type: {type(page)}")
    print(f"\t- content: {page}")
    print(f"\t- utf8 content: {page.decode()}")
