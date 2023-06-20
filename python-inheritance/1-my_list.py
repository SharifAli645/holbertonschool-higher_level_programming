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
        new = self[:]
        new.sort()
        print(new)
