#!/usr/bin/python3
"""checking an object is an instance of class or not"""


def is_kind_of_class(obj, a_class):
    """checking an object is an instance or not
    Args:
        obj: object
        a_class: the class it bleongs
    """
    if isinstance(obj, a_class):
        return True

    return False
