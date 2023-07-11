#!/usr/bin/python3
"""
function that appends a string at the end of text
"""


def append_write(filename="", text=""):
    """
    append a string at the end of utf8 text file

    filename: the name of the file to append
    text: the string to append to the file

    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
