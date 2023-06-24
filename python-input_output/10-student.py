#!/usr/bin/python3
"""
Module
that defines
a Student
"""


class Student:
    """Class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """
        Constructor

        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Function that retrives a dictionary representation
        of a Student instance

        Returns: dictionary representation
        """
        if attrs is None:
            atrb = self.__dict__
        else:
            di = dict()
            for ele in attrs:
                if ele in self.__dict__:
                    di[ele] = self.__dict__.get(ele)
            atrb = di
        return atrb
