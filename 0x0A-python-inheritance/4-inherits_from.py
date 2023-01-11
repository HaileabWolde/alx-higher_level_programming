#!/usr/bin/python3
"""checking an object is an instance of class or not"""


def inherits_from(obj, a_class):
    """checking an object is an instance or not
    Args:
        obj: object
        a_class: the class it bleongs
    """
    if ((isinstance(obj, a_class)) and type(obj) != a_class):
        return (True)
    else:
        return (False)
