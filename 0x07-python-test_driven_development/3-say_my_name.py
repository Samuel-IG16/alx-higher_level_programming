#!/usr/bin/python3
"""
Module say_my_name
Prints a given first name and last name.
"""


def say_my_name(first_name, last_name=""):
    """Prints a string with <first_name>
    and <last_name>.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
