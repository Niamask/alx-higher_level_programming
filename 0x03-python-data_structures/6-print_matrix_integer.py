#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    lenght = len(matrix[0]) 

    if lenght != 0:
        for row in matrix:
            for i in range(lenght - 1):
                print("{:d}".format(row[i]),end=" ")
            print("{:d}".format(row[lenght - 1]))
    else:
        print("")
