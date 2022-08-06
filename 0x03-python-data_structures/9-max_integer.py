#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to find the biggest integer of a list
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------


def max_integer(my_list=[]):
    """
    Args:
        my_list: a list

    Returns:
        the biggest integer in list or none if list is empty
    """

    if len(my_list) == 0:
        return None
    else:
        biggest_int = my_list[0]
        for index in range(len(my_list)):
            if my_list[index] > biggest_int:
                biggest_int = my_list[index]
    return biggest_int
