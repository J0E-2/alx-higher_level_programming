#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
    A function that computes the square values of all integers
    of a matrix.

    Returns a new matrix that is the same size as matrix.
    '''

    new_matrix = [[col**2 for col in row] for row in matrix]
    return (new_matrix)
