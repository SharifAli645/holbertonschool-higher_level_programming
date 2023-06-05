#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for col in matrix:
        f = 0
        for ele in col:
            if f == 0:
                f = 1
            else:
                print(" ", end="")
            print("{:d}".format(ele), end="")
        print("")
