#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to delete the item at a specific position in a list
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------


def delete_at(my_list=[], idx=0):
    """deletes the item at a specific position in a list

    Args:
        my_list: a list
        idx: an integer representing an index position

    Returns:
        list without deleted item
    """

    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list.remove(my_list[idx])
    return my_list
