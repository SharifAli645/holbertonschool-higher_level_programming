#!/usr/bin/python3
"""
Class
that
is empty
"""


class BaseGeometry:
    """
    Class BaseGeometry
    """
    def area(self):
        """
        Function that raise a error

        Raise:
            Exception:
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function that validate an integer

        Args:
            name (string): name
            value (int): integer
        Raise:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
