#!/usr/bin/python3
"""import JSON"""
import json

"""define function"""


def save_to_json_file(my_obj, filename):
    """function writes an object to a text file"""
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(json.dumps(my_obj))
