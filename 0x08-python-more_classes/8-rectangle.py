#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """
    Defines a class Rectangle
        number_of_instances(int):
        print_symbol(str)
    Public class attribute
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle
            width(int): width of rectangle, default is 0
            height(int): height of rectangle, default is 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
            Returns width of a rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the new width of a rec
            value(int)
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Returns the height of a rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Returns the height of a rectangle
            value(int)
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Returns the area of a rectangle
        """
        a = self.__width * self.__height
        return a

    def perimeter(self):
        """
            Returns the perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            perim = 2 * (self.__width * self.__height)
        return perim

    def __str__(self):
        """
            Returns the string representation of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        rect_str = ""
        for _ in range(self.__height):
            rect_str += str(self.print_symbol) * self.__width + "\n"
        return rect_str.rstrip()

    def __repr__(self):
        """
            Return strin representation
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
            Print a message when an instance is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on area
        Args:
            rect_1(int):
            rect_2(int)
        Returns:
            (int): the biggest or smallest of the two rectangles
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
