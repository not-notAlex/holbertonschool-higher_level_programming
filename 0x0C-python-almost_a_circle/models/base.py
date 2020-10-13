#!/usr/bin/python3
"""
module for base class
"""


import json


class Base():
    """
    the base class to inherit from
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns JSON string of dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes JSON string of list_objs to file
        """
        n = cls.__name__ + ".json"
        new_list = []
        if list_objs is not None:
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))
        with open(n, "w") as f:
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """
        returns list of string representation
        """
        if json_string is None or len(json_string) == 0:
            return json.loads("[]")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with attributes set
        """
        if cls.__name__ = "Square":
            new_clone = cls(1)
        else:
            new_clone = cls(1, 1)
        new_clone.update(**dictionary)
        return new_clone

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        n = cls.__name__ + ".json"
        new_list = []
        try:
            with open(n, "r") as f:
                i = cls.from_json_string(f.read())
            for value in i:
                new_list.append(cls.create(**value))
        except:
            pass
        return new_list
