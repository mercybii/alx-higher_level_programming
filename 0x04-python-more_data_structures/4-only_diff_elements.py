#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new_set = set_1 | set_2
    return {item for item in new_set if item in set_1 and item not in set_2 or
            item in set_2 and item not in set_1}
