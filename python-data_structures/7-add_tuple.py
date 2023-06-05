#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = [0, 0]
    i = 0
    l_tuple_a = len(tuple_a)
    l_tuple_b = len(tuple_b)

    while i < 2:
        if l_tuple_a > 0:
            new[i] = new[i] + tuple_a[i]
        l_tuple_a -= 1
        if l_tuple_b > 0:
            new[i] = new[i] + tuple_b[i]
        i += 1
        l_tuple_b -= 1
    return tuple(new)
