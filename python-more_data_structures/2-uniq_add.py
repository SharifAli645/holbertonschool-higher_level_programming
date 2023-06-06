#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    for ele in range(len(my_list)):
        if my_list[ele] in my_list[:ele]:
            continue
        add = add + my_list[ele]
    return add
