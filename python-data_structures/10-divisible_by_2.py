#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    for ele in my_list:
        if ele % 2 == 0:
            new.append(True)
        else:
            new.append(False)
    return new
