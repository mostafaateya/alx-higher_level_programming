#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a = list(a_dictionary.keys())
    for x in a:
        if value == a_dictionary.get(x):
            del a_dictionary[x]
    return (a_dictionary)
