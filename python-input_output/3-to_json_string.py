#!/usr/bin/python3
"""
Module
that works
with
json module
"""


import json


def to_json_string(my_obj):
    """
    Function that returnst the JSON representation of an
    object (string)

    Args:
        my_obj (object): object to transform
    Returns: the JSON representation
    """
    return json.dumps(my_obj)
