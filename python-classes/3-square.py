#!/usr/bin/python3
"""Class that define a geometric figure"""


class Square:
    """
    Represents a square.

    Attributes:
        size (int): size of the square.
    """
    def __init__(self, size=0):
        """
        Constructor.

        Args:
            size (int): size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return (self.__size ** 2)
