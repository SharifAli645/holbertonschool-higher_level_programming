#!/usr/bin/python3
"""
Module that
compares
instances and classes
"""


def inherits_from(obj, a_class):
    """
    Function that verify class of an object

    Args:
        obj (instance): object
        a_class (class): class
    Returns:
        True if verifies it, false otherwise
    """
    if a_class in type(obj).__mro__[1:]:
        return True
    return False
