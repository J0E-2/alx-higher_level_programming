#!/usr/bin/python3
"""import JSON"""
import json

"""define function"""


def from_json_string(my_str):
    """function returns an object represented by a JSON string"""
    return (json.loads(my_str))
