#!/usr/bin/python3
"""define a class 'MyList'"""


class MyList(list):
    """define public instance method that prints a sorted list"""
    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
