#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response.
"""

import requests
from sys import argv

if __name__ == "__main__":
    a = requests.get(argv[1])
    if a.status_code >= 400:
        print("Error code: {}".format(a.status_code))
    else:
        print(a.text)
