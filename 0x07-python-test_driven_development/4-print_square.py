#!/usr/bin/python3
"""Define print_square function"""


def print_square(size):
    """Print a square by # sign and the size is the len of the square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for r in range(size):
        for c in range(size):
            print("#", end="")
        print()
