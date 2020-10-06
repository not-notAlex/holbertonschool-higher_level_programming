#!/usr/bin/python3
"""
module for 7-base_geometry.py
"""


class BaseGeometry():
    """
    geometric shape
    """
    def area(self):
        """
        raises error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value < 1:
            raise ValueError("{:s} must be greater than 0".format(name))
