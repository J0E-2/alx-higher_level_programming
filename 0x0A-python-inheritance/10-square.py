#!/usr/bin/python3
"""import class to use as the base class (Rectangle)"""

Rectangle = __import__('9-rectangle'). Rectangle


class Square(Rectangle):
    """class Rectangle"""

    def __init__(self, size):
        """Instatiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def  area(self):
        return self.__size * self.__size
