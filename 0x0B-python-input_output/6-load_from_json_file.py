#!/usr/bin/python3
"""import JSON"""
import json

"""define function"""


def load_from_json_file(filename):
    """function creates an Object from a "JSON file" """
    with open(filename, "r", encoding="UTF-8") as f:
        json.loads(f.read())
