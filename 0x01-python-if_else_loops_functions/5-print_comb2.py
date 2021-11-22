#!/usr/bin/python3
for num in range(0, 100):
     if num < 10:
        print("{0:0=2d}".format(num), end=", ")
     else:
        print("{0:0=2d}".format(num),  end=", ")
