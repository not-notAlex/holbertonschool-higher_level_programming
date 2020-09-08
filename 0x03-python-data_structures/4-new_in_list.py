#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    last = len(my_list)
    new_list = []
    for i in range(0, last):
        new_list = new_list + [my_list[i]]
        if i == idx:
            new_list[i] = element
    return new_list
