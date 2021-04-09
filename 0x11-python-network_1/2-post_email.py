#!/usr/bin/python3
"""
module for task 2
"""

from sys import argv
import urllib.parse
import urllib.request


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': argv[2]})
    data = data.encode('ascii')
    re = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(re) as r:
        print(r.read().decode('utf-8'))
