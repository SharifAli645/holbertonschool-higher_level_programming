#!/usr/bin/python3
def matrix_divided(matrix, div):
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"
    if type(matrix) != list:
        raise TypeError(msg1)
    for x in range(len(matrix)):
        if type(matrix[x]) != list:
            raise TypeError(msg1)
        if x != len(matrix) - 1:
            if len(matrix[x]) != len(matrix[x + 1]):
                raise TypeError(msg2)
        for k in range(len(matrix[x])):
            if type(matrix[x][k]) not in [int, float]:
                raise TypeError(msg1)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_l = matrix.copy()
    for i in range(len(matrix)):
        new_l[i] = list(map(lambda x: round(x / div, 2), matrix[i]))
    return new_l
