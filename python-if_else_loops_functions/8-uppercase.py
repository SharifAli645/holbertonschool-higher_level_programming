#!/usr/bin/python3
def uppercase(str):
    for letter in range(0, len(str)):
        cl = ""
        if letter == len(str) - 1:
            cl = "\n"
        if ord(str[letter]) > 96 and ord(str[letter]) < 123:
            print("{}".format(chr(ord(str[letter]) - 32)), end=cl)
        else:
            print("{}".format(str[letter]), end=cl)
