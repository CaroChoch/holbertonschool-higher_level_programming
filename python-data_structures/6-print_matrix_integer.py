#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for value in range(len(row)):
            print("{:d}".format(row[value]), end=" ")
        print()
