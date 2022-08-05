#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to do exactly the same as the following Python bytecode:
#
# 3           0 LOAD_FAST                0 (a)
#             3 LOAD_FAST                1 (b)
#             6 COMPARE_OP               0 (<)
#             9 POP_JUMP_IF_FALSE       16

# 4          12 LOAD_FAST                2 (c)
#            15 RETURN_VALUE

# 5     >>   16 LOAD_FAST                2 (c)
#            19 LOAD_FAST                1 (b)
#            22 COMPARE_OP               4 (>)
#            25 POP_JUMP_IF_FALSE       36

# 6          28 LOAD_FAST                0 (a)
#            31 LOAD_FAST                1 (b)
#            34 BINARY_ADD
#            35 RETURN_VALUE

# 7     >>   36 LOAD_FAST                0 (a)
#            39 LOAD_FAST                1 (b)
#            42 BINARY_MULTIPLY
#            43 LOAD_FAST                2 (c)
#            46 BINARY_SUBTRACT
#            47 RETURN_VALUE
#
# demonstrates how to use a function, and an if...elif condition to affect
# program output
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------

# Use `python3 -m py_compile file_name.py` or `python3 -m compileall
# file_name.py` to compile source file
# Bytecode is stored in a .pyc file in a folder named __pycache__ generated
# after compilation
# To view the .pyc file in non binary(human readable) form run
# `python3 -m dis file_name.py` command
# READ:https://towardsdatascience.com/understanding-python-bytecode-e7edaae8734d


def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return (a * b) - c
