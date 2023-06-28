#!/usr/bin/python3
"""class that define a sqare"""


class Square:
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise TypeError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """calculate the square area

        Return:
        the area of the square
        """
        return (self.__size) **2
