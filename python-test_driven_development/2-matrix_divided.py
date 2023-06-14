#!/usr/bin/python3
def matrix_divided(matrix, div):
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    if(type(matrix) not in [list] or type(matrix[0]) not in [list]
            or type(matrix[1]) not in [list]):
        raise TypeError(msg1)
    for element in matrix[0]:
        if type(element) not in [int, float]:
            raise TypeError(msg1)

    for element in matrix[1]:
        if type(element) not in [int, float]:
            raise TypeError(msg1)

    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    c_matrix = []
    for lst in range(len(matrix)):
        c_matrix.append([])
        for ele in range(len(matrix[lst])):
            c_matrix[lst].append(round(matrix[lst][ele] / div, 2))
    return c_matrix
