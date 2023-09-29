#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    x = 0
    y = len(list_of_integers)
    a = ((y - x) // 2) + x
    a = int(a)
    if y == 1:
        return list_of_integers[0]
    if y == 2:
        return max(list_of_integers)
    if list_of_integers[a] >= list_of_integers[a - 1] and\
            list_of_integers[a] >= list_of_integers[a + 1]:
        return list_of_integers[a]
    if a > 0 and list_of_integers[a] < list_of_integers[a + 1]:
        return find_peak(list_of_integers[a:])
    if a > 0 and list_of_integers[a] < list_of_integers[a - 1]:
        return find_peak(list_of_integers[:a])
