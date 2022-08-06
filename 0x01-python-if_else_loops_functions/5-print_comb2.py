#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print numbers from 0 to 99
# demonstrates how to use a loop and string formatting to affect program output
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------

# For each number in range sequence
for number in range(0, 99):

    # Print out number according to fill and width format
    print("{:02d}".format(number), end=", ")

# Print out last number
print(99)
