#!/usr/bin/python3
"""Function prints a text with 2 new lines after character ., ? and :
   Text must be a string"""
def text_indentation(text):
    """No space at the beginning or end of each printed line"""
    if not isinstance(text, str) or text is None:
        raise TypeError('text must be a string')
    for char in text:

        if char in ('.', '?', ':'):
            print('{}\n'.format(char))

        else:
            print(f'{char}', end="")
