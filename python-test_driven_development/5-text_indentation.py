#!/usr/bin/python3
"""To manipulate strings"""


def text_indentation(text):
    """print blankets"""
    if type(text) not in [str]:
        raise TypeError("text must be a string")
    for char in text:
        print("{}".format(char), end="")
        if char in ['.', '?', ':']:
            print("\n\n", end="")
