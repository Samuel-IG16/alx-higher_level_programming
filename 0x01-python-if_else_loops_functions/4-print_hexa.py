#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print all numbers from 0 to 98 in decimal and in
# hexadecimal
# demonstrates how to use a loop to affect program output
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------

# For each number in range sequence
for number in range(99):

    # Print out the number and the hex value of number
    print("{:d} = {}".format(number, hex(number)))
