#!/usr/bin/python3
"""To manipulate strings"""


def text_indentation(text):
    """print blankets"""
    last = ""
    if type(text) not in [str]:
        raise TypeError("text must be a string")
    for char in text:
        if last in ['.', '?', ':'] and char == " ":
            last = ""
            continue
        print("{}".format(char), end="")
        if char in ['.', '?', ':']:
            last = char
            print("\n\n", end="")
            continue
