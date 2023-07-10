#!/usr/bin/python3
"""
is a function that look for attributes
"""


def lookup(obj):
    """
    return list of objects

    obj: are the object to insert
    
    return: list of available attributes and methods
    """
    return dir(obj)
