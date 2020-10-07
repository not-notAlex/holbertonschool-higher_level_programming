#!/usr/bin/python3
"""
module for 4-append_write.py
"""


def append_write(filename="", text=""):
    """
    appends to a file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
