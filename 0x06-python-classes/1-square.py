#!/usr/bin/python3
""" a class called Square that defines a Square by:
(based on 0-square.py)

"""


class Square:
    """
     A Square with a private attribute -
     size
    """
    def __init__(self, size):
        """
         Initializes the size variable as a private instance attribute
        """
        self.__size = size
