#!/usr/bin/python3
"""Define class Rectangle"""


class Rectangle:
    """define object attributes"""
    def __init__(self, width=0, height=0):
        """object instantiation using the init method"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves current width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the current width size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves current height size"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height size"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        else:
            self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the rectangle perimeter if width or
        height is not 0"""
        if self.__width < 0 or self.__height < 0:
            return (0)

        else:
            return (2 * (self.__width + self.__height))
