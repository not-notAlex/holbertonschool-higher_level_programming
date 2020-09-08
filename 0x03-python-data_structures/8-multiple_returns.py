#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    c = ""
    if length > 0:
        c = sentence[0]
    else:
        c = None
    new_tuple = length, c
    return new_tuple
