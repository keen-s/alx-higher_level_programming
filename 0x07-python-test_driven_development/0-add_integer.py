#!/usr/bin/python3
""" Adding the integers """


def add_integer(a, b=98):
    """ Adds two numbers
    Args:
         a - first integer
         b - Second input
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be integer")
    return int(a) + int(b)
