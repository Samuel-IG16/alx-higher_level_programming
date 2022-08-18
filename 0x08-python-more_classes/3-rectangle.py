#!/usr/bin/python3
# -----------------------------------------------------------
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------
"""Rectangle Class.

This module contains an empty class that defines a rectangle.

Usage Example:

    Rectangle = __import__('0-rectangle').Rectangle

    my_rectangle = Rectangle()
    print(type(my_rectangle))
    print(my_rectangle.__dict__)
"""


class Rectangle:
    """Defines the blueprint of a rectangle.

    Attribute:
        width: An integer indicating the width of the rectangle object.
        height: An integer indicating the height of the rectangle object.
    """

    def __init__(self, width=0, height=0):
        """An object constructor method.

        Initiatilizes Rectangle with width and height.

        Args:
            width: An integer representing object width.
                  Has a default value of 0.
            height: An integer representing object height.
                  Has a default value of 0.
        """
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ""
        rec_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += "#"
            rec_str += "\n"
        return rec_str[:-1]

    @property
    def width(self):
        """Gets the width private attribute value.

        Returns:
            The width private attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width private attribute value.

        Validates the assignment of the width private attribute.

        Arg:
            value: the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height private attribute value.

        Returns:
            The height private attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height private attribute value.

        Validates the assignment of the height private attribute.

        Arg:
            value: the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A public object method.

        Returns:
            The current rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """A public object method.

        Returns:
            The current rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
