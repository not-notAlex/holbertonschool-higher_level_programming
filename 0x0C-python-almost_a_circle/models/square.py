#!/usr/bin/python3
"""
module for square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    the square class the inherits from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        square constructor
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        prints representation of square attributes
        """
        output = "[Square] (" + str(self.id) + ") "
        output += str(self.x) + "/" + str(self.y) + " - "
        output += str(self.size)
        return output

    @property
    def size(self):
        """
        size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        upadtes square attributes
        """
        if args:
            count = 0
            for v in args:
                if count == 0:
                    self.id = v
                if count == 1:
                    self.size = v
                if count == 2:
                    self.x = v
                if count == 3:
                    self.y = v
                count += 1
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        returns dictionary of attributes
        """
        new_dict = {"id": self.id, "size": self.size}
        new_dict.update({"x": self.x, "y": self.y})
        return new_dict
