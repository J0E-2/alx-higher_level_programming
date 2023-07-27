#!/usr/bin/python3
""" class BaseGeometry (based on 6-base_geometry.py)"""
class BaseGeometry:
    """
    Public instance method: def area(self): raises an
    Exception with the message area() is not implemented
    """
    def area(self):
        """raises an excepton"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Public instance method: def integer_validator
        (self, name, value): that validates value"""
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        elif value <= 0:
            raise ValueError(f'{name} must be greater than 0')
        
