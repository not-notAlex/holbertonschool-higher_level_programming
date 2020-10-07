#!/usr/bin/python3
"""
module for 9-add_item.py
"""


import json
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    my_list = list(load_from_json_file('add_item.json'))
except Exception:
    my_list = []
for i in range(1, len(argv)):
    my_list.append(argv[i])
save_to_json_file(my_list, 'add_item.json')
