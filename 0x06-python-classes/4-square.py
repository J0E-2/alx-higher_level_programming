#!/usr/bin/python3
""" Define my class Square"""


class Square:
    """create template of an instance"""
    def __init__(self, size=0):
        """Initializes a new square"""
        self.size = size

    @property
    def size(self):
        """Get current size value"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """check size value"""
        if type(value) is int:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

        else:
            raise TypeError('size must be an integer')

    def area(self):
        """Return the current area of the square"""
        return (self.__size * self.__size)
