#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the are of a square"""
        return self.__size ** 2

    @property
    def size(self):
        """Retrieves the size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size property

        Args:
            value (int): The size of the new square.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

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
