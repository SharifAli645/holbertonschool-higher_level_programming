#!/usr/bin/python3
"""
Module
that contains
a base
Class
"""

import json


class Base:
    """Class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor

        Args:
            id (int): id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns a JSON string"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
