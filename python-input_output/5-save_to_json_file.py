#!/usr/bin/python3
"""
Module
that handles
Files
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file,
    using a JSON representation

    Args:
        filename (string): the file's name
        my_obj (object): Python object
    """
    with open(filename, 'w', encoding='utf-8') as fle:
        fle.write(json.dumps(my_obj))
