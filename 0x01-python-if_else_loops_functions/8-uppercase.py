#!/usr/bin/python3
def uppercase(str):
    for h in str:
        h = ord(h)
        if 97 <= h <= 122:
            h = h - 32
        print("{:c}".format(h), end='')
    print()
