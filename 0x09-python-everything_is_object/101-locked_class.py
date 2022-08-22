#!/usr/bin/python3
"""A locked class that only lets the user dynamically create the instance
    attribute 'first_name'"""


class LockedClass:
    """A locked class that only lets the user dynamically create the instance
    attribute 'first_name'"""
    __slots__ = ["first_name"]

    def __init__(self, first_name=""):
        self.first_name = first_name
