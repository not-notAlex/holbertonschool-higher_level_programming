#!/usr/bin/python3
"""
module for task 9
"""

from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(r.json().get('id'))
