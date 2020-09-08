#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    last1 = len(matrix)
    for i in range(0, last1):
        last2 = len(matrix[i])
        for j in range(0, last2):
            print("{:d}".format(matrix[i][j]), end="")
            if j < (last2 - 1):
                print(" ", end="")
        print()
