#!/usr/bin/python3
"""
Function def pascal_triangle(n): that returns a list
of lists of integers representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """
    Function def pascal_triangle(n): that returns a list
    of lists of integers representing the Pascal’s triangle of n.
    """

    if n <= 0:
        return []

    row = [[1]]  # first row is always just 1
    for x in range(1, n):  # for every other row:
        m = [1]  # it always starts with 1
        for y in range(1, x):  # for all the others:
            m.append(row[x - 1][y - 1] + row[x - 1][y])
            """work out what the number is"""
        m.append(1)  # it always ends in 1
        row.append(m)  # add the row on
    return row
