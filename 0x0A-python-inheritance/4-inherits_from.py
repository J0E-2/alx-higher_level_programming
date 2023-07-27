#!/usr/bin/python3
"""Function returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False"""
def inherits_from(obj, a_class):
    """isinstance checks to see if an object is an instance of a class or a class that was inherited from
       type checks for objects that are not inherited and are exactly an instance of the specified class
    issubclass checks to see if an object's class is a subclass of a specified class"""
    return isinstance(obj, a_class) and type(obj) != a_class and issubclass(type(obj), a_class)
