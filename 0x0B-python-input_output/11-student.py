#!/usr/bin/python3
"""
module for 11-student.py
"""


class Student():
    """
    basic Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        initializes class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns dict version of class
        """
        return self.__dict__
