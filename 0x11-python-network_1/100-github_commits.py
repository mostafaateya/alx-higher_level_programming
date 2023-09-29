#!/usr/bin/python3
""" evaluates candidates applying for a back-end
position with multiple technical challenges,
like this one:"""

import requests
from sys import argv

if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    a = requests.get(url)
    xx = a.json()
    for x in xx[:10]:
        print(x.get('sha'), end=': ')
        print(x.get('commit').get('author').get('name'))
