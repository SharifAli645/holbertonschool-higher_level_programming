#!/usr/bin/python3
'''Represent geometric figures'''


class Rectangle():
    '''Represent a rectangle'''
    def __init__(self, height=0, width=0):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """
        Getter of height

        Returns:
            Height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter of height

        Args:
            value (int): height of the rectangle
        Raises
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        Getter of width

        Returns:
            Width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter of width

        Args:
            value (int): width of the rectangle
        Raises
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
