#!/usr/bin/python3

"""
module 2-matrix_divided
"""


def matrix_divided(matrix, div):
    """
    divides matrix by div
    """
    row = 0
    i = 0
    new_list = [[], []]
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) != 2:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if isinstance(matrix[0], list):
        row = len(matrix[0])
    for x in matrix:
        if not isinstance(x, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(x) != row:
            raise TypeError("Each row of the matrix must have the same size")
        for y in x:
            if not isinstance(y, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_list[i].append(round(y / div, 2))
        i += 1
    return new_list
