#!/usr/bin/python3
""" Creating a class called MyList """


class MyList(list):
    """ A class called MyList that inherits from list """
    def print_sorted(self):
        """ A public instance method that prints
            the list , but sorted(ascending sort)
        """
        print(sorted(self))
