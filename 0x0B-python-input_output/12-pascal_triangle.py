#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n."""
    if n <= 0:
        return []

    xx = [[1]]
    while len(xx) != n:
        xx1 = xx[-1]
        xx2 = [1]
        for i in range(len(xx1) - 1):
            xx2.append(xx1[i] + xx1[i + 1])
        xx2.append(1)
        xx.append(xx2)
    return xx
