#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    if matrix is not None:
        for i in matrix:
            new_matrix.append([*map(lambda x: x * x, i)])
        final = [*new_matrix]
        return final
