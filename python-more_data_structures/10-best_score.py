#!/usr/bin/python3
def best_score(a_dictionary):
    player = None
    if a_dictionary:
        keys = a_dictionary.keys()
        mx = -1
        for ele in keys:
            if a_dictionary.get(ele) > mx:
                mx = a_dictionary.get(ele)
                player = ele
    return player
