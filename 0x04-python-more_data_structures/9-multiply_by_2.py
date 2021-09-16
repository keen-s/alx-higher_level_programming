def multiply_by_2(a_dictionary):
    """
    A function that returns a new dictionary
    with all values multiplied by 2
    """
    nwdct = {}
    for key, value in a_dictionary.items():
        nwdct.update({key: (value * 2)})
    return nwdct
