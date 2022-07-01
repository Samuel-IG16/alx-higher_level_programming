#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def main():
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1
    else:
        a = argv[1]
        op = argv[2]
        b = argv[3]
        if op == "+":
            print("{} + {} = {}".format(a, b, add(int(a), int(b))))
        elif op == "-":
            print("{} - {} = {}".format(a, b, sub(int(a), int(b))))
        elif op == "*":
            print("{} * {} = {}".format(a, b, mul(int(a), int(b))))
        elif op == "/":
            print("{} / {} = {}".format(a, b, div(int(a), int(b))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            return 1


if __name__ == "__main__":
    main()
