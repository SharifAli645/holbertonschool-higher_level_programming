#!/usr/bin/python3
"""
Class Square that inherits from Rectangle class,
size must be private and must be a positive integer and
the area() must be implemented
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that defines a Square
    """
    def __init__(self, size):
        """Constructor of Square class

        Args:
            size (int): the size of the square
        """
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """
        Function that calculates the area

        Returns: the area of a square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Function __str__

        Returns: representation of the instance
        """
        return f"[Square] {self.__size}/{self.__size}"
