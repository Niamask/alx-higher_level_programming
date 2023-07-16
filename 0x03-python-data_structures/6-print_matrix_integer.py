#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    tail = len(matrix[0])
    if tail != 0:
        for ligne in matrix:
            for i in range(tail - 1):
                print("{:d}".format(ligne[i]), end=" ")
            print("{:d}".format(ligne[tail - 1]))
    else:
        print("")
