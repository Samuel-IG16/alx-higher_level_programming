#!/usr/bin/python3
"""Module 11-square.
Creates a Square class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square.
    Private instance attribute size.
    Public method area().
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """Initializes a Square.

        Args:
            - size: size of the square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return str("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Computes the area of a Square instance.
        Overwrites the area() method from Rectangle.
        """

        return self.__size ** 2
