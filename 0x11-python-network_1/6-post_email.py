#!/usr/bin/python3
"""
module for task 6
"""

from sys import argv
import requests

if __name__ == "__main__":
    p = {'email': argv[2]}
    r = requests.post(argv[1], data=p)
    print(r.text)
