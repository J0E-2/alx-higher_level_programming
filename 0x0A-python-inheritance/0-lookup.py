#!/usr/bin/python3
"""Define class lookup"""
def lookup(obj):
    """returns the list of available attributes and methods""" 
    return list(obj.__dict__)
