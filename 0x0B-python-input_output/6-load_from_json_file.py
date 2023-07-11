#!/usr/bin/python3
"""
function that creates an object from json
"""


import json


def load_from_json_file(filename):
    """
    cointain the load_from_json
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
