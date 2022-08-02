#!/usr/bin/python3
"""Module 2-read_lines.
Reads a certain number of lines from a file.
"""


def read_lines(filename="", nb_lines=0):
    """Reads and prints nb_lines lines from filename.

    Args:
        - filename: name of the file
        - nb_lines: number of lines to read
    """

    with open(filename) as f:
        i = 0
        count = 0
        for line in f:
            count += 1
        f.seek(0)
        if nb_lines <= 0 or nb_lines >= count:
            read_text = f.read()
            print(read_text, end="")
        else:
            for line in f:
                print(line, end='')
                i += 1
                if i == nb_lines:
                    break
