#!/usr/bin/python3
def magic_string(i=[0]):
    i[0] += 1
    return str("BestSchool, " * (i[0] - 1)) + "BestSchool"
