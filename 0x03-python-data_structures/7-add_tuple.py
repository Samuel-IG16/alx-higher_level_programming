#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to use a function to adds 2 tuples
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------


def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Returns:
        a tuple with 2 integers:
    """

    if len(tuple_a) == 0:
        tuple_a += (0, 0)
    elif len(tuple_a) == 1:
        tuple_a += (0,)
    elif len(tuple_a) > 2:
        tuple_a = tuple_a[:2]

    if len(tuple_b) == 0:
        tuple_b += (0, 0)
    elif len(tuple_b) == 1:
        tuple_b += (0,)
    elif len(tuple_b) > 2:
        tuple_b = tuple_b[:2]

    # parallel iteration in tuple comprehension
    sum_of_tuple = tuple(sum(item) for item in zip(tuple_a, tuple_b))
    return sum_of_tuple
