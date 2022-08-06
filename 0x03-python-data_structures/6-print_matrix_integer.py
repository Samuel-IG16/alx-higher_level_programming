#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print a matrix of integers
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------


def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers

    Args:
        matrix: a matrix
    """

    # If no argument is supplied print a newline
    if not matrix:
        print()
    else:
        # Loop through the rows
        for row in matrix:
            # Loop through the items in row
            for item in row:
                # Add space between items if not last item in row
                if row.index(item) != len(row) - 1:
                    endspace = " "
                else:
                    endspace = ""
                # Print the items in the row
                print("{:d}".format(item), end=endspace)
            print()
