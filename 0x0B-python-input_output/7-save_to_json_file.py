#!/usr/bin/python3
"""
module for 7-save_to_json_file.py
"""


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file
    """
    import json
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
