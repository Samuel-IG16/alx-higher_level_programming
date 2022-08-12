#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print an integer with "{:d}".format()
# demonstrates how to use a try ... except for exception handling
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        return False

    return True
