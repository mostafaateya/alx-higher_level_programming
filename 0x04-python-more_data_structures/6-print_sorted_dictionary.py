#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = list(a_dictionary.keys())
    a.sort()
    for x in a:
        print("{}: {}".format(x, a_dictionary.get(x)))
