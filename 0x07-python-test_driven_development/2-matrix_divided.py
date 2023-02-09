#!/usr/bin/python3
"""
Test driven development
"""
def matrix_divided(matrix, div):
    """
    function divides all elements of a matrix
    
    @matrix: matrix whose elements are to be divided
    @div: integer to divide with

    Returns: a new matrix
    """
    
    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_length = len(matrix[0])

    new = []
    for row in matrix:
        length = 0
        newmatrix = []
        for col in row:
            if type(col) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            newmatrix.append(round((col / div), 2))
            length += 1

        if length != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        new.append(newmatrix)

    return (new)
