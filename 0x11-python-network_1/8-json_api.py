#!/usr/bin/python3
"""
module for task 8 
"""

from sys import argv
import requests

if __name__ == "__main__":
    if len(argv) < 2:
        l = ""
    else:
        l = argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data={'q': l})
    try:
        new_dict = r.json()
        if new_dict:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
