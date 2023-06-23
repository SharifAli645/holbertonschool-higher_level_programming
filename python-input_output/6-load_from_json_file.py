#!/usr/bin/python3
"""
Module
that handles
Files
"""

import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a JSON file

    Args:
        filename (string): the file's name
    Returns:
        Object from a “JSON file”
    """
    with open(filename, 'r', encoding='utf-8') as fle:
        return json.loads(fle.read())
