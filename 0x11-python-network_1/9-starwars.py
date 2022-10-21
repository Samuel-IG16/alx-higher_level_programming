#!/usr/bin/python3
"""
Use requests package to make a get request to the swapi api.
Use string argument as search value of request. Body response must
be JSON and formatted to a Python dictionary.
"""
import sys
import requests

if __name__ == "__main__":
    url = "https://swapi.co/api/people/?search={}".format(sys.argv[1])
    r = requests.get(url).json()
    print("Number of result: {}".format(r['count']))
    for c in r['results']:
        print(c['name'])
