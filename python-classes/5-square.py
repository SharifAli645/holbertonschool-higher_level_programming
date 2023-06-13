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

    @property
    def size(self):
        """
        Getter of size

        Returns:
            Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of size

        Args:
            value (int): size of the square
        Raises
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints the square.
        """
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for e in range(self.__size):
                print("{}".format("#"), end="")
            print("")
