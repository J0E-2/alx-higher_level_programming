#!/usr/bin/python3
"""import BaseGeometry class from 7-base_geometry file"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class inherits from our base class BaseGeometry
    """
    def __init__(self, width, height):
        """instatiation with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f'[Rectangle] {self.__width}/{self.__height}'
