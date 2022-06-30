#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    else:
         print("{} arguments: ".format(len(argv) - 1))
         for item in argv:
             if argv.index(item) == 0:
                 continue
             print("{}: {}".format(argv.index(item), item))
