#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''
    function adds all unique integers in a list (only
    once for each integer).
    '''
    new_list = set(my_list)
    sum = 0

    for item in new_list:
        sum += item

    return (sum)
