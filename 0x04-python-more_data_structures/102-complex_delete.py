#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to delete keys with a specific value in a dictionary
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------


def complex_delete(a_dictionary, value):
    for idx in list(a_dictionary.keys()):
        if a_dictionary[idx] == value:
            del a_dictionary[idx]
    return a_dictionary
