#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = set(my_list)
    s = 0
    for x in a:
        s += x
    return (s)
