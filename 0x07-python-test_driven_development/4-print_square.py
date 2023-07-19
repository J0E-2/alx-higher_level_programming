#!/usr/bin/python3
"""
    Funcion prints a square with the character #
    size is the size length of the square
    siz emust be an int and greater than zero
"""

def print_square(size):
    """size represents the size of square to be printed

    size must be an integer and be not less than 0"""
    if not isinstance(size, (int, float)):
        raise TypeError('size must be an integer')

    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')

    elif size < 0:
        raise ValueError('size must be >= 0')

    for row in range(size):
        print("")
        for col in range(size):
            print('#', end="")

            if row == size - 1 and col == size - 1:
                print("")
