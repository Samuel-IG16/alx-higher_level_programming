#!/usr/bin/python3
# -----------------------------------------------------------
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------
"""Square Class.

This module contains a class that defines a square.

Usage Example:

    Square = __import__('102-square').Square

    s_5 = Square(5)
    s_6 = Square(6)
    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
"""


class Square:
    """Defines the blueprint of a square.

    Attribute:
        size (int): An integer representing the object size.
    """

    def __init__(self, size=0):
        """An object constructor method."""
        self.__size = size

    @property
    def size(self):
        """Gets the size private attribute value.

        Returns:
            The size private attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size private attribute value.

        Validates the assignment of the size private attribute.

        Arg:
            value: the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """A public object method.

        Returns:
            The current square area
        """
        return self.__size**2

    def __eq__(self, o):
        """Defines the == comparison"""
        return self.__size == o.__size

    def __ne__(self, o):
        """Defines the != comparison"""
        return self.__size != o.__size

    def __gt__(self, o):
        """Defined the > comparison"""
        return self.__size > o.__size

    def __ge__(self, o):
        """Defined the >= comparison"""
        return self.__size >= o.__size

    def __lt__(self, o):
        """Defined the < comparison"""
        return self.__size < o.__size

    def __le__(self, o):
        """Defined the <= comparison"""
        return self.__size <= o.__size
