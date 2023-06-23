#!/usr/bin/python3
"""
Module
that handles
Files
"""


def append_write(filename="", text=""):
    """
    Function that adds content to the end of
    a file

    Args:
        filename (string): the name's file
        text (string): the content to add
    Returns: The number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as fle:
        fle.write(text)
    return len(text)
