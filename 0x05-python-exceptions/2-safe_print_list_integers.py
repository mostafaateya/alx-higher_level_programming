#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    a = 0
    for z in range(0, t):
        try:
            print("{:d}".format(my_list[z]), end="")
            a += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (a)
