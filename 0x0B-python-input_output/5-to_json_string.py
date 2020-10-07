#!/usr/bin/python3
"""
module for 5-to_json_string.py
"""


def to_json_string(my_obj):
    """
    prints json format of object
    """
    import json
    return json.dumps(my_obj)
