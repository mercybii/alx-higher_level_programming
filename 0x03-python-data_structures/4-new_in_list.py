#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    i = 0
    for ele in my_list:
        if i == idx:
            new_list[i] = element
            i += 1
            return (new_list)
