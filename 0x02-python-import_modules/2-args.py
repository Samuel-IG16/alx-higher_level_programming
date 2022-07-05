#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    if n == 1:
        print("{:d} {}.".format(0, "arguments"))
    elif n == 2:
        print("{:d} {}:".format(1, "argument"))
        for i in range(1, n):
            print("{:d}: {}".format(n - 1, sys.argv[i]))
    else:
        print("{:d} {}:".format(n - 1, "arguments"))
        for i in range(1, n):
            print("{:d}: {}".format(i, sys.argv[i]))
