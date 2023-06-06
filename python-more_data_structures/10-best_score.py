#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    keys = a_dictionary.keys()
    mx = -9999
    pr = ""
    for ele in keys:
        if a_dictionary.get(ele) > mx:
            mx = a_dictionary.get(ele)
            pr = ele
    return pr
