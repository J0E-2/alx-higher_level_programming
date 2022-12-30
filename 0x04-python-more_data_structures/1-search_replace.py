#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
    Function replaces all occurrences of an element by another
    in a new list.
    
    my_list is the initial list
    search is the element to replace in the list
    replace is the new element
    '''
    new_list = []

    for item in my_list:
        if item == search:
            item = replace
        new_list.append(item)

    return(new_list)
