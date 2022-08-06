#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print prints the ASCII alphabet, in reverse order,
# alternating lowercase and uppercase (z in lowercase and Y in uppercase)
# demonstrates how to use a loop and an if...elif condition to affect
# program output
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------

# Define the loop with lowercase letters starting from last letter
# first lowercase letter has odd ascii_code
# last lowercase letter has even ascii_code
# For odd ascii_codes convert letters to uppercase

# For ascii_code in range sequence
for ascii_code in range(122, 96, -1):

    # If ascii_code is odd
    if ascii_code % 2 == 1:

        # Convert letter to uppercase
        ascii_code = ascii_code - 32

    # Print out letters
    print("{:c}".format(ascii_code), end="")
