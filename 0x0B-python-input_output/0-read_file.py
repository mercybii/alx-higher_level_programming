#!/usr/bin/python3
"""
read a text file
"""
def read_file(filename=""):
    """
    read a text file (utf8)
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
