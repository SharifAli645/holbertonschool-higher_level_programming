#!/usr/bin/python3
"""Aritmetic operations"""


def add_integer(a, b=98):
    """
    Adds two numbers and returns the result.

    Args:
        a (int): first number
        b (int): second number
    Raises:
        TypeError: If one arg is not a number
    Returns:
        int: the result to add a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
