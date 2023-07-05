#!/usr/bin/python3
"""
a mode of a rectangle
"""


class Rectangle:
    """
    is a class that repressent the class of rectangle
    """

    def __init__(self, width=0, height=0):
        """
        initialization of the :

        width
        height
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getting the width of the rectanglr
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getting the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setting the height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
