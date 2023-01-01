#!/usr/bin/python3
def safe_print_integer(value):
    """
    function that prints an integer with "{:d}".format().
    value can be any type (integer, string, etc.)
    The integer should be printed followed by a new line

    Returns True if value has been correctly printed (it
    means the value is an integer)
    Otherwise, returns False
    """
    try:
        print("{:d}".format(value))

    except (TypeError, ValueError):
        return (False)

    else:
        return (True)
