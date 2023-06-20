#!/usr/bin/python3
"""
Module that
compares
instances and classes
"""


def is_same_class(obj, a_class):
    """
    Function that verify class of an object

    Args:
        obj (instance): object
        a_class (class): class
    Returns:
        True if verifies it, false otherwise
    """
    if type(obj) == a_class:
        return True
    return False
