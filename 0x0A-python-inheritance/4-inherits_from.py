#!/urs/bin/python3
"""
class inherutance
"""


def inherits_from(obj, a_class):
    """
    class that inherited from tge specified class

    obj: the class to check
    a_class: the class to compare againts

    retturn: true if the object is an insance
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
