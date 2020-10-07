#!/usr/bin/python3
"""
module for 6-from_json_string.py
"""


def from_json_string(my_str):
    """
    returns object from json string
    """
    import json
    return json.loads(my_str)
