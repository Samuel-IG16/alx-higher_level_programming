#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to retrieve an element from a list like in C
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------


def element_at(my_list, idx):
    """Retrieves an element from a list like in C

    Args:
        my_list: a list
        idx: the index of item to retrieve

    Returns:
        the item at index idx
    """

    # Check for negative and out of range index
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    return my_list[idx]
