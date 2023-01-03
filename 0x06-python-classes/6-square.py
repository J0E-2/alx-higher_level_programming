#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """class Square definition"""
    def __init__(self, size=0, position=(0, 0)):
        """initialization of a class square instance"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve current position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set current position"""
        if (len(value) != 2 or type(value) is not tuple
            or type(value[0]) is not int or
            type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Returns the current area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with the character #:
         and an empth line if the size is 0"""
        if self.__size == 0:
            print("")

        for k in range(self.__position[1]):
            print()

        else:
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")

                for j in range(self.__size):
                    print("#", end="")

                print("")
