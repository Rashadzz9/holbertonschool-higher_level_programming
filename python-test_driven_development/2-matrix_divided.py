#!/usr/bin/python3
"""Module for matrix division"""

 
def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div"""
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or not matrix:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(msg)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
