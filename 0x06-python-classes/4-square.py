#!/usr/bin/python3
""" class defination of a square"""


def __init__(self, size=0):
    """"attributes and methodwes"""
    self.size = size


def area(self):
    """the area of the square"""


return (self.__size) ** 2


@property
def size(self):
    """the getter of the size"""
    return self.__size


@size.setter
def size(self, value):
    """the setter of the size"""
    if type(value) is not int:
        raise TypeError("size must be an integer")
    else:
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
