#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print the ASCII alphabet in lowercase except 'q' and 'e'
# demonstrates how to use a loop, a loop clause and an if condition to
# affect program output
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------

# For each ascii_code in range sequence
for ascii_code in range(97, 123):

    # If ascii_code match code for 'q' and 'e' skip it
    if ascii_code == 101 or ascii_code == 113:
        continue

    # Print out the character format of the ascii_code
    print("{:c}".format(ascii_code), end='')
