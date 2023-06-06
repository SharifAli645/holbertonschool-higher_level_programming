#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for ele in my_list:
        if ele == search:
            new.append(replace)
        else:
            new.append(ele)
    return new
