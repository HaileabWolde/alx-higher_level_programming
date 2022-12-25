#!/usr/bin/python3
# 2-square.py writeen by Haileab Woma


class Square:

    """ a blue print for the instances of square"""

    def __init__(self, size=0):

        """ creates object or instances of classes
            Args:
                size: size of th square
            Raises:
                TypeError: if size is not integer
                ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ method for calculating area of object of class
            Returns: The sqaure of the size
        """
        return (self.__size) * (self.__size)
