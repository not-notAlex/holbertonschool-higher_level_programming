#!/usr/bin/python3

"""
module 4-square
defines class square
"""


class Square:
    """
    defiens class square
    """
    def __init__(self, size=0):
        """
        inits square
        size: the size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        returns size property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets size property
        value: the new size value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        return area of the square
        """
        return (self.__size ** 2)
