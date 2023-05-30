#!/bin/python3
e = 0
i = 0
var = ""
var1 = ", "
while i < 10:
    print("{}{}".format(e, i), end="")

    if e == 9 and i == 9:
        var = "\n"
        var1 = ""
    print("{}".format(var1), end=var)
    if e == 9 and i == 9:
        break

    if e != 9 and i == 9:
        i = 0
        e = e + 1
    else:
        i = i + 1
