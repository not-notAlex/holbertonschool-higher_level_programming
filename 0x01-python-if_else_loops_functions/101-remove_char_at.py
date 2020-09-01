#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    newstr = ""
    for c in str:
        if i != n:
            newstr += c
        i += 1
    return newstr
