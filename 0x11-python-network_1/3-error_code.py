#!/usr/bin/python3
"""
module for task 3
"""

from sys import argv
import urllib.request

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as r:
            print(r.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
