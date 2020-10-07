#!/usr/bin/python3
"""
module for 0-read_file.py
"""


def read_file(filename=""):
    """
    reads whole file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
