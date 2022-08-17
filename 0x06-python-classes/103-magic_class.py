#!/usr/bin/python3
# -----------------------------------------------------------
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------
"""MagicClass.

This module contains code representing a circle.

Usage Example:

    MagicClass = __import__('103-magic_class').MagicClass

    a_circle = MagicClass(5)
    print(a_circle.area())
"""
import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return self.__radius**2 * math.pi

    def circumference(self):
        """Return The circumference of the MagicClass."""
        return 2 * math.pi * self.__radius
