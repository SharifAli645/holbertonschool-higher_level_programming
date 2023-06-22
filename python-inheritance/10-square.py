#!/usr/bin/python3
"""
Module
that defines
geometric figures
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class
    that defines
    a Square
    """
    def __init__(self, size):
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        """
        Function that calculates the area

        Returns: the area of a square
        """
        return self.__size ** 2

    def __str__(self):
        msg = "[Rectangle] {}/{}"
        return msg.format(self.__size, self.__size)
