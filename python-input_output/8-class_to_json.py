#!/usr/bin/python3
"""
Module
that works
with Json
and Classes
"""


def class_to_json(obj):
    """
    Function that returns dict of properties of an instance

    Returns: the dict of properties
    """
    return obj.__dict__
