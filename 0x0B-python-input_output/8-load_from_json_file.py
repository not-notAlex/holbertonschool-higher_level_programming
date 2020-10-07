#!/usr/bin/python3
"""
module for 8-load_from_json_file.py
"""


def load_from_json_file(filename):
    """
    creates an object from json file
    """
    import json
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
