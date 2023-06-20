#!/usr/bin/python3
"""
Subclass
from
SuperClass
List
"""


class MyList(list):
    """Class that inheritances from List Parent Class"""
    def print_sorted(self):
        """
        Function that print an ordered list

        """
        new = self[:]
        new.sort()
        print(new)
