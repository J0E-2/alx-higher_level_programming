#!/usr/bin/python3
"""import JSON"""
import json

"""define function"""


def to_json_string(my_obj):
    """function returns the JSON representation of an object"""
    return(json.dumps(my_obj))
