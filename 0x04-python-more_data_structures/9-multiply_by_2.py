#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {item: (a_dictionary[item])*2 for item in list(a_dictionary)}
    return new_dic
