#!/usr/bin/python3
"""Class that define a geometric figure"""


class Square:
    """
    Represents a square.
    ...

    Attributes
    ----------
    size : int
        size of the square

    """
    def __init__(self, size):
        """
        Constructor.

        Parameters
        ----------
            size : int
                size of the square
        """
        self.__size = size
