#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = a_dictionary.copy()
    k = list(a.keys())
    for x in k:
        a[x] *= 2
    return (a)
