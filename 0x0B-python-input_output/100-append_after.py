#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file."""
    a = ""
    with open(filename) as xx:
        for line in xx:
            a += line
            if search_string in line:
                a += new_string
    with open(filename, "w") as w:
        w.write(a)
