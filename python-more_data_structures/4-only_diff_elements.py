#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = list(set_1) + list(set_2)
    new_1 = list()
    for i in new:
        if new.count(i) == 1:
            new_1.append(i)
    return set(new_1)
