#!/usr/bin/python3
import sys
import json
from typing import List
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def add_item(filename: str, item: str) -> None:
    try:
        items = load_from_json_file(filename)
    except:
        items = []
    items.append(item)
    save_to_json_file(items, filename)

if __name__ == '__main__':
    args = sys.argv[1:]
    for arg in args:
        add_item("add_item.json", arg)
