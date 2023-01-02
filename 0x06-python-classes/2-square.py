#!/usr/bin/python3
"""
a class Square that defines a square by: (based on 1-square.py)
     Private instance attribute: size
     Instantiation with optional size: def __init__(self, size=0):
     size must be an integer, otherwise raise a TypeError
        exception with the message size must be an integer
     if size is less than 0, raise a ValueError exception
        with the message size must be >= 0
"""


class Square:
    """creating an object template"""
    def __init__(self, size=0):
        """
        The init method initializes the class instance

        @self:
               A parameter used to refer to the class instance

        @size:
               the size of the square
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size

        else:
            raise TypeError('size must be an integer')
