#!/usr/bin/python3
def fizzbuzz():
    val = " "
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz", end=val)
        elif i % 5 == 0:
            print("Buzz", end=val)
        elif i % 3 == 0:
            print("Fizz", end=val)
        else:
            print(i, end=val)
