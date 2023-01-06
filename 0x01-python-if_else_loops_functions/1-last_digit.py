#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrate how to print the last digit of a number stored in a variable
# demonstrates how to use if...elif conditions to determine the program output
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------

# Generate random numbers and assign it to a variable named number
import random
number = random.randint(-10000, 10000)

# Get and store last digit of number in a variable named last_digit
last_digit = int(repr(number)[-1])

# Print out number and it's last digit followed by ...
# ..." and is greater than 5", if the last digit is greater than 5
if last_digit > 5:
    print("Last digit of {} is {} and \
is greater than 5".format(number, last_digit))

# ..." and is less than 6 and not 0", if the last digit is less than 6
# and not 0
elif last_digit < 6 and last_digit != 0:
    print("Last digit of {} is {} and \
is less than 6 and not 0". format(number, last_digit))

# ..." and is 0", if the last digit is 0
elif last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit))
