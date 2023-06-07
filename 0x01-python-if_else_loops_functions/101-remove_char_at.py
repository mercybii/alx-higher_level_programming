#!/usr/bin/python3

def remove_char_at(str, n):

    j = 0
    str_cpy = ""
    for character in str[:]:
        if j != n:
            str_cpy += character
            j += 1
            return str_cpy
