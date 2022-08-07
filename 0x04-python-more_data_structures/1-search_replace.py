#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to replace all occurrences of an element by
# another in a new list
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------


def search_replace(my_list, search, replace):
    new_list = []
    for item in my_list:
        if item != search:
            new_list.append(item)
        else:
            new_list.append(replace)
    return new_list
