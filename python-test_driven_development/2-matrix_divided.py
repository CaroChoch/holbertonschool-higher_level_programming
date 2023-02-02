#!/usr/bin/python3
""" Function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix: list of lists of integers or floats.
        div: a number (integer or float).

    Return: a new matrix divided by div
    Raise:
        TypeError: if matrix is not a list of lists of integers or floats,
            or if div is not a number.
        TypeError: if each row of the matrix is not of the same size.
        ZeroDivisionError: if div = 0.
    """

    message = "matrix must be a matrix (list of lists) of integers/floats"

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(message)
    elif not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError(message)
    elif not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
