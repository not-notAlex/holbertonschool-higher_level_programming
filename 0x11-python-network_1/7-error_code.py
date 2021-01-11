#!/usr/bin/python3
"""
module for task 7
"""

from sys import argv
import requests

if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code < 400:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
