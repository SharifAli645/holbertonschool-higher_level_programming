#!/usr/bin/python3
"""
Aritmetic

operations
"""


def add_integer(a, b=98):
    """
    Adds two numbers and returns the result.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
