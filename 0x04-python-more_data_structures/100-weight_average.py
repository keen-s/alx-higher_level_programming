def weight_average(my_list=[]):
    size_avg = 0
    size = 0
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    for tup in my_list:
        size_avg += (tup[0] * tup[1])
        size += tup[1]
    return (size_avg / size)
