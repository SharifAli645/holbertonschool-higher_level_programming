#!/usr/bin/python3
"""
Module
that defines
geometric figures
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class
    that defines
    a rectangle
    """
    def __init__(self, width, height):
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
