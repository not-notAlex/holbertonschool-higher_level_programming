#!/usr/bin/python3
"""
Module 1-rectangle
Defines class Rectangle
"""


class Rectangle:
    """
    defines Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        inits square
        width: the width of the square
        height: height of the square
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """
        returns height property
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        gives height new value
        value: sets height to vlaue
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        returns width property
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        gives width new value
        value: sets width to vlaue
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """
        returns area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        prints the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect = ""
            for x in range(0, self.__height):
                for y in range(0, self.__width):
                    rect += "#"
                rect += "\n"
            rect = rect[0:-1]
            return rect

    def __repr__(self):
        """
        returns string to reproduce this rectangle
        """
        output = "Rectangle("
        output += str(self.__width)
        output += ", "
        output += str(self.__height)
        output += ")"
        return output

    def __del__(self):
        """
        says goodbye to dead rectangle
        """
        print("Bye rectangle...")
