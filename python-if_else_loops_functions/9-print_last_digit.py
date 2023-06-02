#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        num = abs(number) % 10
        print("{}".format(num), end="")
    else:
        num = number % 10
        print("{}".format(num), end="")
    return(num)
