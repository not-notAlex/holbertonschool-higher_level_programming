#!/usr/bin/python3

"""
module 3-square
defines class square
"""


class Square:
    """
    defines class square
    """
    def __init__(self, size=0):
        """
        inits square
        size: the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        returns area of the square
        """
        return self.__size ** 2
