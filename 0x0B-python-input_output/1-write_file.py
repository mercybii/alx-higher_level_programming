#!/usr/bin/python3
"""
function that write a string text file
"""


def write_file(filename="", text=""):
    """
    append a string to the end of utf8 text
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
