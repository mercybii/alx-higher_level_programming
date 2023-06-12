#!/usr/bin/python3

def multiple_returns(sentence):
    len = len(sentence)
    if len == 0:
        char = None
    else:
        char = sentence[0]
        return ((len, char))
