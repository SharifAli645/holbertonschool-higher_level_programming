#!/usr/bin/python3
def multy(a, b):
    return a * b


def multiply_list_map(my_list=[], number=0):
    num = []
    for i in range(len(my_list)):
        num.append(number)
    new = map(multy, my_list, num)
    return list(new)
