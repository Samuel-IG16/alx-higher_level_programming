#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to import a function def add(a, b): from the
# file add_0.py and print the result of the addition 1 + 2 = 3
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------

# Import the add function
from task import add

a = 1
b = 2

# This code should not run when this file is imported
if __name__ == "__main__":
    print("{:d} + {:d} = {:d}". format(a, b, add(a, b)))
