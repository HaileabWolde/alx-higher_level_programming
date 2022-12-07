#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:  # to print multi-dimension array
        for j in i:
            if j != 0:
                print(" ", end='')
            print("{:d}".format(j), end=" ")
        print()
