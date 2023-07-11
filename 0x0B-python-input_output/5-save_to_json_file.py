#!/usr/bin/python3
"""
function that write an object to a text file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    write an object to text a file
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
