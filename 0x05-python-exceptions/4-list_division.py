#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    a = []
    for z in range(0, list_length):
        try:
            out = my_list_1[z] / my_list_2[z]
        except TypeError:
            print("wrong type")
            out = 0
        except ZeroDivisionError:
            print("division by 0")
            out = 0
        except IndexError:
            print("out of range")
            out = 0
        finally:
            a.append(out)
    return (a)
