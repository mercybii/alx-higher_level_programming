#!/usr/bin/python3

def multiple_returns(sentence):
    s_len = len(sentence)
    if s_len == 0:
        char = None
    else:
        char = sentence[0]
    return ((s_len, char))
