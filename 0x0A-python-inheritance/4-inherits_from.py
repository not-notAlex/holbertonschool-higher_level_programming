#!/usr/bin/python3
"""
module for 4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """
    detects if object is inherited from class
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
