#!/usr/bin/python3
"""It reutrns true if the object is exactly or else false"""


def is_same_class(obj, a_class):
    """Initalizing of this class
    Args:
        obj: repersents the objected number
        a_class: the class that is to be checked
    """
    return (type(obj) == a_class)
