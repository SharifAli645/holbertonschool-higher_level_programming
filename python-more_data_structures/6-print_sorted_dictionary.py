#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = sorted(a_dictionary)
    for ele in new:
        print("{}: {}".format(ele, a_dictionary.get(ele)))
