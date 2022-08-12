#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print the result of dividing 2 integers
# demonstrates how to use a try ... except ... finally for exception handling
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------


def safe_print_division(a, b):
    try:
        div = a / b
    except (ZeroDivisionError, FloatingPointError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
