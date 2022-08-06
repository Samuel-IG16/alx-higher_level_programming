#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to determine if a number stored in a variable is
# positive or negative
# demonstrates how to use if...elif conditions to determine the program output
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------

# Generate random numbers and assign it to a variable named number
import random
number = random.randint(-10, 10)

# Print out the value of number followed by ...
# ..." is positive", if number is greater than zero
if number > 0:
    print("{} is positive".format(number))

# ..." is negative", if number is less than zero
elif number < 0:
    print("{} is negative".format(number))

# ..." is zero", if number is equals to zero
else:
    print("{} is zero".format(number))
