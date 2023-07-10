#!/usr/bin/python3
"""
is a module that provide a function for checking is an object is an instance
"""


def is_kind_of_class(obj, a_class):
    """
    a function that return true if the object is an instance of or
    id the object is an intance of a class

    obj: is the object to check
    a_class:  the class to compare
    """
    if isinstance(obj, a_class):
        return True
    return False
