#!/usr/bin/python3
"""
function that return true 
"""


def is_same_class(obj, a_class):
    """
    check if the object are exactly an instances

    obj: is the object to check
    a_class: is the class to match the type

    Returns: true when an oject is exactly otherwise false
    """
    if type(obj) == a_class:
        return True
    return False
