#!/usr/bin/python3
def uppercase(str):
    for str in str:
        if (ord(str) >= 97 and ord(str) <= 122):
            str = chr(ord(str) - 32)
            print("{:s}".format(str), end="")
    print()
