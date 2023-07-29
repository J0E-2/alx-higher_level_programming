#!/usr/bin/python3
"""
import BaseGeometry class from 7-base_geometry file



"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class inherits from our base class BaseGeometry
    """
    def __init__(self, width, height):
        """
        instatiation with width and height
        width and height must be private
        the two attributes are validated by integervaliadtor
        from base class
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        implementation of the area method
        returns area of triangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        returns '[Rectangle] <width>/<height>' when
        used with print)
        """
        return f'[Rectangle] {self.__width}/{self.__height}'
