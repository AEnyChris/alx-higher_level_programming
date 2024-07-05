#!/usr/bin/python3
"""Write a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    username = str(argv[1])
    password = str(argv[2])

    url = 'https://api.github.com/user'
    resp = requests.get(url, auth=(username, password))
    output = resp.json()
    print(f"{output.get('id')}")
