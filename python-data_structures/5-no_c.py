#!/usr/bin/env python3
def no_c(my_string):
    new_str = []
    for ch in my_string:
        new_str.append(ch)
    ct = 0
    while ct < len(new_str):
        if new_str[ct] == 'c' or new_str[ct] == 'C':
            new_str.pop(ct)
            ct = 0
        ct += 1
    return new_str
