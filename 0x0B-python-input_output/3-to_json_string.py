#!/usr/bin/python3
"""
function that return json
"""


import json


def to_json_string(my_obj):
    """
    retun the json represention of an object
    """
    return json.dumps(my_obj)
