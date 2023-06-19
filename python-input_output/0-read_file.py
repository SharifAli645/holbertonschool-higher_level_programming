#!/usr/bin/python3
"""
Module
that handles
Files
"""


def read_file(filename=""):
    """
    Function that print the content of a file

    Args:
        filename (string): the name's file
    """
    with open(filename) as fle:
        print(fle.read(), end="")
