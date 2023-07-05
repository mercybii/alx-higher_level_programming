#!/usr/bin/python3
"""
Define the class rectangle
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        initization of the rectangle

        width
        height
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            """
            setting the width of the rectangle
            """
            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            if value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value

        @property
        def height(self):
            """
            rectangle for the new rectangle
            """
            if not isinstance(value, int):
                raise TypeError('heigth must be an integer')
            if value < 0:
                raise ValueError('height must be >= 0')
            seif.__height = value

        def area(self):
            """
            the area of the rectanle
            """
            if self.__width == 0 or self.__height == 0:
                return 0
            else:
                perim = 2 * (self.__width + seif.__height)
            return perim
