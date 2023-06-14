#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    dict = {}
    for key, val in a_dictionary.items():
        dict[key] = val * 2
    return dict
