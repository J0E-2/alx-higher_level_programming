#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"

    i = 0
    for letter in my_list:
        if letter > i:
            i = letter

    return(i)
