#!/usr/bin/python3
"""Module 101-add_attribute.
Checks if an attribute can be added to an object.
"""


def add_attribute(an_obj, an_attr, a_value):
    """Checks if an_attr of value a_value can be added to an_obj.

    Args:
        - an_obj: object to add the attribute to
        - an_attr: name of the attribute
        - a_value: value of the attribute to add
    """

    if not hasattr(an_obj, '__slots__') and not hasattr(an_obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if hasattr(an_obj, '__slots__') and not hasattr(an_obj, an_attr):
        raise TypeError("can't add new attribute")

    setattr(an_obj, an_attr, a_value)
