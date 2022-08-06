#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print the smallest, unique combinations of two digits
# demonstrates how to use loops and an if condition to affect program output
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------

# Digits are 0 ... 9
# Loop variables to increment:  first_digit, second_digit
# For smallest combination first_digit < second_digit
# For unique combination first_digit != second_digit
# For smallest unique combination !(second_digit <= first_digit)

for first_digit in range(0, 8):
    for second_digit in range(0, 10):
        if not (second_digit <= first_digit):
            print("{:d}{:d}".format(first_digit, second_digit), end=", ")

# Print last values for first_digit and second_digit
print("89")
