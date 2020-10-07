#!/usr/bin/python3
"""
module for 14-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    returns pascal triangle list
    """
    my_list = [1]
    output = [[1]]
    if n <= 0:
        return []
    for i in range(1, n):
        new_list = my_list.copy()
        for j in range(1, len(new_list)):
            my_list[j] = new_list[j] + new_list[j - 1]
        my_list.append(1)
        output.append(my_list.copy())
    return output
