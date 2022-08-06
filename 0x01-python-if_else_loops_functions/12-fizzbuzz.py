#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print the numbers from 1 to 100 separated by a space
# demonstrates how to use a function, a loop and an if...elif condition to
# affect program output
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------


def fizzbuzz():
    """Print out numbers from 1 to 100"""

    # For number in range sequence
    for number in range(1, 101):

        # If number is a multiple of three
        if number % 3 == 0 and number % 5 != 0:

            # Print out "Fizz "
            print("Fizz ", end="")

        # If number is a multiple of five but not of three
        elif number % 5 == 0 and number % 3 != 0:

            # Print out "Buzz "
            print("Buzz ", end="")

        # If number is a multiple of both three and five
        elif number % 15 == 0:

            # Print out "FizzBuzz "
            print("FizzBuzz ", end="")

        else:
            # Print number
            print("{:d} ".format(number), end="")
