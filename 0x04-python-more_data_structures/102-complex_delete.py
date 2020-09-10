#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    words = {}
    for i, j in a_dictionary.items():
        if j != value:
            words[i] = j
    a_dictionary.clear()
    for i, j in words.items():
        a_dictionary[i] = j
    return a_dictionary
