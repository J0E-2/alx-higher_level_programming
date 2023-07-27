#!/usr/bin/python3
"""
Class based on 5-base_geometry.py
"""
class BaseGeometry:
    """
    Public Instance method that raises an exception with the
    message area() is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")
