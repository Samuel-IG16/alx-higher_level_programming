#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to delete a key in a dictionary
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
