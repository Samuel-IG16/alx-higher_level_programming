#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to return a key with the biggest integer value
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------


def best_score(a_dictionary):
    if not a_dictionary:
        return (None)

    return (max(a_dictionary, key=a_dictionary.get))
