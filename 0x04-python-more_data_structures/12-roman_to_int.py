#!/usr/bin/python3
def differance(a):
    x = 0
    max_a = max(a)
    for z in a:
        if max_a > z:
            x += z
    return (max_a - x)


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    a_keys = list(a.keys())
    i = 0
    j = 0
    k = [0]
    for x in roman_string:
        for y in a_keys:
            if y == x:
                if a.get(x) <= j:
                    i += differance(k)
                    k = [a.get(x)]
                else:
                    k.append(a.get(x))
                j = a.get(x)
    i += differance(k)
    return (i)
