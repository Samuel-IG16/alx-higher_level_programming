#!/usr/bin/python3
"""
Use requests package to make a get request to given URL and display
the value of `X-Request-Id` in response header.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('x-request-id'))
