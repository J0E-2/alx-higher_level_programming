#!/usr/bin/python3
"""Function divides all elements of a matrix
   
   Returns a New List
   
   matrix must be a list of lists of integers or floats otherwi   se raises an Exception"""

def matrix_divided(matrix, div):
    if not isinstance(matrix, list) or len(matrix) is 0 or matrix is None:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    if not isinstance(div, (int, float)):
         raise TypeError('div must be a number')


    for row in matrix:
        len1 = len(matrix[0])
        len2 = len(row)

        if len(row) == 0:
            raise TypeError('matrix must be a matrix (list \
of lists) of integers/floats')

        if len1 != len2:
            raise TypeError('Each row of the matrix must have the same size')

        for col in row:
            if type(matrix) is not list or not isinstance(col, (int, float)) or not isinstance(row, list):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

 
    new = [[round(col / div, 2) for col in row if type(div) is int or float] for row in matrix if div != 0 and type(matrix) is list]
    return new
