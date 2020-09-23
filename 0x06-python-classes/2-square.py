#!/usr/bin/python3

"""
module 2-square
defines a square
"""


class Square:
    """
    Defines class square

    """
    def __init__(self, size=0):
        """
        inits square
        size: the size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
