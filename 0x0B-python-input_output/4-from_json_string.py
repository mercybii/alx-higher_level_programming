#!/usr/bin/python3
"""
function that return an object
"""


import json


def from_json_string(my_str):
    """
    return an object to represent by a json
    """
    return json.loads(my_str)
