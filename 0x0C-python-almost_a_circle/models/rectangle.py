#!/usr/bin/python3
"""
module for rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """
    the rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        constrcutor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """
        x setter
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """
        y setter
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        returns area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        prints the rectangle
        """
        for j in range(0, self.__y):
            print()
        for x in range(0, self.__height):
            for k in range(0, self.__x):
                print(" ", end="")
            for y in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        returns format of object info
        """
        output = "[Rectangle] (" + str(self.id) + ") "
        output += str(self.__x) + "/" + str(self.__y) + " - "
        output += str(self.__width) + "/" + str(self.__height)
        return output

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if args:
            count = 0
            for value in args:
                if count == 0:
                    self.id = value
                if count == 1:
                    self.width = value
                if count == 2:
                    self.height = value
                if count == 3:
                    self.x = value
                if count == 4:
                    self.y = value
                count += 1
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        returns dictionary of attributes
        """
        new_dict = {"id": self.id, "width": self.width}
        new_dict.update({"height": self.height, "x": self.x, "y": self.y})
        return new_dict
