#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to return the weighted average of all integers tuple
# (<score>, <weight>)
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------


def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    div = 0
    for tup in my_list:
        average += tup[0] * tup[1]
        div += tup[1]
    return float(average / div)
