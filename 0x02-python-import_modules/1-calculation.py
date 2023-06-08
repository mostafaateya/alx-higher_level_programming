#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    x1 = 10
    x2 = 5
    print("{} + {} = {}".format(x1, x2, add(x1, x2)))
    print("{} - {} = {}".format(x1, x2, sub(x1, x2)))
    print("{} * {} = {}".format(x1, x2, mul(x1, x2)))
    print("{} / {} = {}".format(x1, x2, div(x1, x2)))
