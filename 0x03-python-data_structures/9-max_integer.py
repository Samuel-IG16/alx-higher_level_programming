#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    biggest = 0
    for index in my_list:
        if index > biggest:
            biggest = index
    return biggest
