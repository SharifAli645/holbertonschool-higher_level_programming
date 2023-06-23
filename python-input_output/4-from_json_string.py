#!/usr/bin/python3
"""
Module
that works
with
json module
"""


import json


def from_json_string(my_str):
    """
    Function that returns a Python data structure

    Args:
        my_str (str): JSON string
    Returns: Python data structure
    """
    return json.loads(my_str)
