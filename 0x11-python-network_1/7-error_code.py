#!/usr/bin/python3
"""
Use requests package to make a get request to given URL and display
the body of response, or error code if error.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    try:
        r.raise_for_status()
        print(r.text)
    except Exception as e:
        print("Error code: {}".format(r.status_code))
