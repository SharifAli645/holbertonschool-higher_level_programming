#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    num = [number]
    num = num * len(my_list)
    new = map(lambda x, y: x * y, my_list, num)
    return list(new)
