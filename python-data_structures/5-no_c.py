#!/usr/bin/env python3
def no_c(my_string):
    new_str = ""
    ct = 0
    for ch in my_string:
        if ch == 'c' or ch == 'C':
            continue
        else:
            new_str += ch
    return new_str
