#!/usr/bin/python3
"""
module for 13-student.py
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

    def to_json(self, attrs=None):
        """
        returns dict version of class
        """
        if attrs is None:
            return self.__dict__
        my_dict = self.__dict__
        new_dict = {}
        for k, v in my_dict.items():
            if k in attrs:
                new_dict.update({k: v})
        return new_dict

    def reload_from_json(self, json):
        """
        replaces all attributes of Student
        """
        for k, v in json.items():
            setattr(self, k, v)
