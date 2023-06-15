#!/usr/bin/python3
def text_indentation(text):
    for char in text:
        print("{}".format(char), end="")
        if char in ['.', '?', ':']:
            print("\n")
