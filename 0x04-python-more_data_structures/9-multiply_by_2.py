#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nwdct = {}
    for key, value in a_dictionary.items():
        nwdct.update({key: (value * 2)})
    return nwdct
