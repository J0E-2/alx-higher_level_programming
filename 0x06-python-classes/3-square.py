#!/usr/bin/python
"""
    A class Square that defines a square by:
    Private instance attribute: size
    Instantiation with optional size:
                   def __init__(self, size=0):
"""


class Square:
    """creating an object template"""
    def __init__(self, size=0):
        """
        object initialization using the init method

        @self:
            parameter used to refer to the class instance

        @size:
            size of the square
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size

        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        Public instance method that returns the current
        square area
        """
        return (self.__size**2)
