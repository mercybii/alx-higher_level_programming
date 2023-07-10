#!/usr/bin/python3
"""
contain class basegeometry
"""


class BaseGeometry:
    """
    class basegeometry with public instance
    """
    def area(self):
        """
        raise an eception when called
        """
        raise Exception("area() is not implemented")

    def intrger_validator(self, name, value):
        """
        validate that the value is an intager
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
