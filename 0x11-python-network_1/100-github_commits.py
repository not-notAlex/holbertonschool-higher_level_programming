#!/usr/bin/python3
"""
module for task 10
"""

from sys import argv
import requests

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        argv[2], argv[1])
    r = requests.get(url)
    new_dict = r.json()
    for i in new_dict[0:10]:
        print(i.get('sha'), end=': ')
        print(i.get('commit').get('author').get('name'))
