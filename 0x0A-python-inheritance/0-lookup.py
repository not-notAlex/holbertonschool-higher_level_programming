#!/usr/bin/python3
"""
module for 0-lookup.py
"""

def lookup(obj):
    """
    prints attributes and methods of an object
    """
    return list(obj.__dict__)
