#!/usr/bin/python3
def uniq_add(my_list=[]):
    li = []
    x = 0
    for i in my_list:
        if i not in li:
            x += i
            li.append(i)

    return x
