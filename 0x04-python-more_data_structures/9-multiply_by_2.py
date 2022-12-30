#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    function that returns a new dictionary with all values
    multiplied by 2

    You can assume that all values are only integers
    Returns a new dictionary
    """
    new_dic = {item: (a_dictionary[item])*2 for item in list(a_dictionary)}
    return new_dic
