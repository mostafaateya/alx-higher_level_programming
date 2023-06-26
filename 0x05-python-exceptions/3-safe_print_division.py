#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        out = a / b
    except (TypeError, ZeroDivisionError):
        out = None
    finally:
        print("Inside result: {}".format(out))
    return (out)
