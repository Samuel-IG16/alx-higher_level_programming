#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print the number of commandline arguments
# and the list of its arguments
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------

# import sys module to access argv
from sys import argv

# Determine the length of argv excluding item at index 0
argv_length = len(argv) - 1

# This code should not run when this file is imported
if __name__ == "__main__":
    # Print out different statements based on length
    if argv_length > 1:
        print("{:d} arguments:".format(argv_length))
    elif argv_length == 0:
        print("{:d} arguments.".format(argv_length))
    else:
        print("{:d} argument:".format(argv_length))

    # Loop through and print out item and it's index
    for arg_item in argv:
        if argv.index(arg_item) == 0:
            continue
        print("{:d}: {}".format(argv.index(arg_item), arg_item))
