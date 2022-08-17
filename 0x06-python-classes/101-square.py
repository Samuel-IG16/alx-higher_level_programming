#!/usr/bin/python3
# -----------------------------------------------------------
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------
"""Square Class.

This module contains a class that defines a square.

Usage Example:

    Square = __import__('101-square').Square

    my_square = Square(5, (0, 0))
    print(my_square)
    print("--")
    my_square = Square(5, (4, 1))
    print(my_square)
"""


class Square:
    """Defines the blueprint of a square.

    Attribute:
        size (int): An integer representing the object size.
        position (int, int): The position of the new square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """An object constructor method."""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Gets the position private attribute value.

        Returns:
            The position private attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position private attribute value.

        Validates the assignment of the position private attribute.

        Arg:
            value: the value to be set
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """A public object method.

        Returns:
            The current square area
        """
        return self.__size**2

    def my_print(self):
        """Displays the square object with # character"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Print the square with the # character."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ""
