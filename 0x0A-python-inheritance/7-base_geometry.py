#!/usr/bin/python3
"""A classs that raises execption"""


class BaseGeometry:
    """A class that raise exceptions"""

    def area(self):
        """a method that intialize itself"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a method that validates if integer or not
        Args:
            name: a name
            value: a value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

        self.name = name
        self.value = value
