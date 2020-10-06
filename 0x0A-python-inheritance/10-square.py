#!/usr/bin/python3
"""
module for 10-square.py
"""


Rectangle = __import__('9-rectangle').Rectangle



class Square(Rectangle):
    """
    a geometric square
    """
    def __init__(self, size):
        """
        initializes square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        returns area of square
        """
        return self.__size ** 2
