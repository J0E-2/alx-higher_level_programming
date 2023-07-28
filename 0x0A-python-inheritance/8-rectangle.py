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
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
