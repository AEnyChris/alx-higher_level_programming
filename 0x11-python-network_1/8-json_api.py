#!/usr/bin/python3
"""Write a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    payload = {'q': q}

    resp = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        output = resp.json()
        if output:
            print(f"[{output['id']}] {output['name']}")
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
