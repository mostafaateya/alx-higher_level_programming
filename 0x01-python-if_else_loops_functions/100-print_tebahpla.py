#!/usr/bin/python3
z = 0
for x in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(x - z)), end="")
    z = 32 if z == 0 else 0
