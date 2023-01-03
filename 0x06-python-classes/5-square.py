#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """class Square definition"""
    def __init__(self, size=0):
        """initialization of a class square instance"""
        self.size = size

    @property
    def size(self):
        """Returns the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of a square

        Args:
            value: first parameter

        Raises:
            TypeError: if value is not an int
            ValueError: if value is less than 0
        """
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the current area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with the character #:
        and an empth line if the size is 0"""
        if self.__size == 0:
            print("")

        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
