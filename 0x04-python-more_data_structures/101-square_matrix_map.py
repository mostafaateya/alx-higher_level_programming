#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda x1: list(map(lambda x2: x2**2, x1)), matrix)))
