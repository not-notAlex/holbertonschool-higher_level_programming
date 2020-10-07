#!/usr/bin/python3
"""
module for 1-number_of_lines.py
"""


def number_of_lines(filename=""):
    """
    returns number of lines in a file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        counter = 0
        for line in f:
            counter += 1
    return counter
