#!/usr/bin/python3

def fizzbuzz():
    for num in range(1, 100):
        if num % 3 == 0:  
           print("fizz", end=" ")
        elif num % 5 == 0:
           print("fuzz", end=" ")
        elif num % 15 == 0:
           print("fizzbuzz", end=" ")
        else:
            print (num, end=" ")
