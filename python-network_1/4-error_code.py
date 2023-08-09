#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
Usage: ./4-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import urllib.error
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    request = requests.Request(url)
    try:
        with requests.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))