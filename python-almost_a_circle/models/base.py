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

    @classmethod
    def save_to_file(cls, list_objs):
        """Class methos that adds the JSON string representation of
        instances to a file"""
        new = []
        if list_objs is not None:
            for ele in list_objs:
                new.append(ele.to_dictionary())
        with open("{}.json".format(cls.__name__), 'w') as fle:
            fle.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        """Static method that returns a list"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method that that returns an instance with all
        attributes already set:"""
        if cls.__name__ == "Rectangle":
            clase = cls(1, 1)
        elif cls.__name__ == "Square":
            clase = cls(1)

        clase.update(**dictionary)
        return clase
