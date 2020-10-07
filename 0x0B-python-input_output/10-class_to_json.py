#!/usr/bin/python3
"""
module for 10-class_to_json.py
"""


def class_to_json(obj):
    """
    returns dict description of json object
    """
    return obj.__dict__
