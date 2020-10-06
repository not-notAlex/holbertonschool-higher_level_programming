#!/usr/bin/python3
"""
module for 8-rectangle.py
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
