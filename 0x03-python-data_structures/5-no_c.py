#!/usr/bin/python3
def no_c(my_string):
    a = [e for e in my_string if e != 'c' and e != 'C']
    return ("".join(a))
