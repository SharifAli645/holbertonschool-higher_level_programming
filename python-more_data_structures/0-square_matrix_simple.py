#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    col = []
    for i in range(len(matrix)):
        col.append([])
        col[i] = [number*number for number in matrix[i]]
    return col
