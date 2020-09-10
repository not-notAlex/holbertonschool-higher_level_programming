#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[]]
    x = 0
    y = 0
    for i in matrix:
        if x != 0:
            new_matrix.append([])
        for j in matrix[x]:
            new_matrix[x].append(j * j)
        x += 1
    return new_matrix
