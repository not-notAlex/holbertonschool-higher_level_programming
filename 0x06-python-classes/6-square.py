#!/usr/bin/python3

"""
module 6-square
defines square class
"""


class Square:
    """
    defines square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        inits square
        size: the size of the square
        position: where to print the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        returns size property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        gives size new value
        value: sets size to vlaue
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        returns position property
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets property value
        value: new tuple for position
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not isinstance(value[0], int) \
           or not isinstance(value[1], int) or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        returns area of square
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        prints square to console
        """
        if self.__size == 0:
            print()
            return
        for j in range(0, self.__position[1]):
            print()
        for x in range(0, self.__size):
            for k in range(0, self.__position[0]):
                print(" ", end="")
            for y in range(0, self.__size):
                print("#", end="")
            print()
