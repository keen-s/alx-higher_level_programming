#!/usr/python3
def common_elements(set_1, set_2):
    for i in set_1:
        if i in set_2:
            set_4 = []
            set_4.append(i)
    return set(set_4)
