#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = matrix.copy()
    for x in range(len(matrix)):
        a[x] = list(map(lambda y: y**2, matrix[x]))
    return (a)
