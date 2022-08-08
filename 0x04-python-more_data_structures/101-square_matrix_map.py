#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to compute the square value of all integers of a matrix
# using map
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------


def square_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(lambda i: i ** 2, x)), matrix))
