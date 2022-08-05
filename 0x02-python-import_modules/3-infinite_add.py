#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print the result of the addition of all
# commandline arguments
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------

# Import sys module to access argv
from sys import argv

# Initialize sum to zero
sum = 0

# This code should not run when this file is imported
if __name__ == "__main__":

    # Iterate through the arguments
    for nums in argv:

        # Skip the first argument
        if argv.index(nums) == 0:
            continue
        # Sum all other arguments
        sum += int(nums)

    # Print out sum
    print(sum)
