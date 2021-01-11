#!/usr/bin/python3
"""
module for task 1
"""

from sys import argv
import urllib.request

if __name__ == "__main__":
    re = urllib.request.Request(argv[1])
    with urllib.request.urlopen(re) as r:
        print(r.getheader('X-Request-Id'))
