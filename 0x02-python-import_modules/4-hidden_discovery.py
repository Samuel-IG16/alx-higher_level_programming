#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print all the names defined by the compiled module
# using dir() hidden_4.pyc (please download it locally)
#
# (C) 2022 Igbinijesu Samuel, Lagos, Nigeria
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------

# Import hidden_4
import hidden_4

# This code should not run when this file is imported
if __name__ == "__main__":

    # Iterate through list of defined names in module
    for def_name in dir(hidden_4):
        if def_name[:2] != "__":
            print(def_name)
