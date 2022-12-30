#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    function prints a dictionary by ordered keys.

    Keys are sorted by alphabetic order

    Only sorts keys of the first level (doesn’t sort keys of a
    dictionary inside the main dictionary)
    """

    for item in sorted(a_dictionary):
        print("{}: {}".format(item, a_dictionary[item]))
