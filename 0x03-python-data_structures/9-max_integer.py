#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    lrg = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > lrg:
            lrg = my_list[i]
    return (lrg)
