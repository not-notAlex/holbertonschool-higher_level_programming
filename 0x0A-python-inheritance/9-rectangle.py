#!/usr/bin/python3
"""
module for 9-rectangle.py
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    rectangle shape
    """
    def __init__(self, width, height):
        """
        initializes object
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        returns the area of shape
        """
        return self.__width * self.__height

    def __str__(self):
        """
        returns formatted string of rectangle
        """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
