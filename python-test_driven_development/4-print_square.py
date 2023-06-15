#!/usr/bin/python3
"""Prints geometric figures"""


def print_square(size):
    """Prints a square"""
    if type(size) is [float] and size < 0:
        raise TypeError("size must be an integer")
    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for e in range(size):
        for i in range(size):
            print("#", end="")
        print()
