#!/usr/bin/python3
"""A class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle inheritng from parent class"""

    def __init__(self, width, height):
        """a properties of width and height"""

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
