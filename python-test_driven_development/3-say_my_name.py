#!/usr/bin/python3
""" Print a message """


def say_my_name(first_name, last_name=""):
    """Print the information of a person"""
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
