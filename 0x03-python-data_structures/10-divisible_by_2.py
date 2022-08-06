#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to find all multiples of 2 in a list
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------


def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list

    Args:
        my_list: a list

    Returns:
        a new list with True or False
    """

    new_list = []
    for index in range(len(my_list)):
        if my_list[index] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
