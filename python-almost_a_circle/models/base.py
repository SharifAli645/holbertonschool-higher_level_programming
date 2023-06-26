#!/usr/bin/python3
"""
Module
that contains
a base
Class
"""


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
