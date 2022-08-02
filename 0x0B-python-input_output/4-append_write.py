#!/usr/bin/python3
"""Module 4-append_write.
Appends a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """Appends text to filename.

    Args:
        - filename: name of the file
        - text: text to append

    Returns: the number of characters added
    """

    with open(filename, 'a+') as f:
        return f.write(text)
