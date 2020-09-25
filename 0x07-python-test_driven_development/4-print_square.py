#!/usr/bin/python3

"""
module 4-print_square
"""


def print_square(size):
    """
    prints a square of certain size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(0, size):
        for y in range(0, size):
            print("#", end="")
        print()
