#!/usr/bin/python3
# 1-square.py Haileab Woldemarim
""" module on defining class Square"""


class Square:
    """class on the defintion of square"""

    def __init__(self, size=0):

        """creating instance of the class square
        Args:
            size: represents the size of the object
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
            """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
