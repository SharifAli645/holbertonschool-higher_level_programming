#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = dict()
    keys = a_dictionary.keys()
    for ele in keys:
        new.update({ele: a_dictionary.get(ele) * 2})
    return new
