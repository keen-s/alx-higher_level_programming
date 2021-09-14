#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lst = []
    for i in my_list:
        if i % 2:
            lst = lst + [False]
        else:
            lst = lst + [True]
    return lst
