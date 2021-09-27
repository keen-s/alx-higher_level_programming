#!/usr/bin/python3
# Writting a function that prints x elements in a list
def safe_print_list(my_list=[], x=0):
    list_count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            list_count += 1
        except IndexError:
            break
    print("")
    return list_count
