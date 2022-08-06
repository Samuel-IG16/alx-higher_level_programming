#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print the last digit of a number
# demonstrates how to use a function to affect program output
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------


def print_last_digit(number):
    """Prints last digit of number

    Args:
        number: a number

    Returns:
        last_digit: the value of the last digit
    """

    # Get and store last digit of number in a variable named last_digit
    last_digit = int(repr(number)[-1])

    # Print out and return the value of last_digit
    print("{}".format(last_digit), end="")
    return last_digit
