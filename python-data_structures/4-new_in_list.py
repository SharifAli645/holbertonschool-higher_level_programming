#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = list()
    for ele in my_list:
        new_list.append(ele)
    if idx < 0 or len(my_list) < idx:
        pass
    else:
        new_list[idx] = element
    return new_list
