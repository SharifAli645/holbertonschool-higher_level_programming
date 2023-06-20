#!/usr/bin/python3
"""
Module that
compares
instances and classes
"""


def is_kind_of_class(obj, a_class):
    """
    Function that verify class of an object

    Args:
        obj (instance): object
        a_class (class): class
    Returns:
        True if verifies it, false otherwise
    """
    if a_class in type(obj).__mro__:
        return True
    return False
