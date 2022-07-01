#!/usr/bin/python3
from sys import argv
summ = 0
if __name__ == "__main__":
    for nums in argv:
        if argv.index(nums) == 0:
            continue
        summ += int(nums)
    print(summ)
