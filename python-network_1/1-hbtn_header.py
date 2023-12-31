#!/usr/bin/python3
""" Display the x-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py<URL>"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    request = requests.Request(url)
    with requests.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))