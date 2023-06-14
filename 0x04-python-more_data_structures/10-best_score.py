#!/usr/bin/python3

def best_score(a_dictionary):
    first = 0
    second = None
    if type(a_dictionary) is dict:
        for (key, value) in a_dictionary.items():
            if value > first:
            first = value
            second = key
    return (second)
