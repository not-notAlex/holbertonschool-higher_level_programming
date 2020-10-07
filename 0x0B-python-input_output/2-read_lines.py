#!/usr/bin/python3
"""
module for 2-read_lines.py
"""


def read_lines(filename="", nb_lines=0):
    """
    reads select number of lines from file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for i in range(0, nb_lines):
                print(f.readline(), end="")
