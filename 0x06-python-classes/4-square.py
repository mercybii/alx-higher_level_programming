#!/usr/bin/python3
""" class defination of a square"""


class Square:
    """class of the square
    attributes:
        side of the square
        """
    def __init__(self, size=0):
        """"attributes and methodwes"""

        self.__size = size

    @property
    def size(self):
        """the getter of the size"""
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size ** 2
