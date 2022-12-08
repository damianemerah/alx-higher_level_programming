#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        el = []
        for j in i:
            el.append(j*j)
        new_matrix.append(el)
    return new_matrix
