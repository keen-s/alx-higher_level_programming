#!/usr/bin/python3
""" Is object present? """


def is_same_class(obj, a_class):
    """A function that returns True if the object is exactly
       an instance of the specified class; otherwise False
    """
    if isinstance(type(obj), a_class):
        return True
    return False
