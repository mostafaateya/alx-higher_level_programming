#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            a.append(True)
        else:
            a.append(False)
    return (a)
