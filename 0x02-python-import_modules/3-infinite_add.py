#!/usr/bin/python3
from sys import argv
summ = 0
for nums in argv:
    if argv.index(nums) == 0:
        continue
    summ += eval(nums)
print(summ)
