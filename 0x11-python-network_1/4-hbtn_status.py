#!/usr/bin/python3
"""This module makes a request to a given url
using the requests module
"""

if __name__ == "__main__":
    import requests

    resp = requests.get('https://alx-intranet.hbtn.io/status')

    print("Body response:")
    print(f"\t- type: {type(resp.text)}")
    print(f"\t- content: {resp.text}")
