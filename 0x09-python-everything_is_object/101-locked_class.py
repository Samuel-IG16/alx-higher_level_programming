#!/usr/bin/python3
class LockedClass:
    """A locked class that only lets the user dynamically create the instance
    attribute 'first_name'"""

    __slots__ = ["first_name"]
