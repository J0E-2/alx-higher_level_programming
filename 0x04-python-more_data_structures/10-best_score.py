#!/usr/bin/python3
def best_score(a_dictionary):
    temp = 0
    if a_dictionary is None:
        return None

    for key, value in a_dictionary.items():
        if value > temp:
            temp = value

    for item in list(a_dictionary):
        if a_dictionary[item] == temp:
            return item
