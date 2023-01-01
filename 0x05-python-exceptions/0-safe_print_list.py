#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    function prints x elements of a list.
    my_list can contain any type (integer, string, etc.)
    All elements are printed on the same line followed by a
    new line.
    x represents the number of elements to print
    x can be bigger than the length of my_list
    Returns the real number of elements printed
    """
    i = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            i += 1

        except IndexError:
            break
    print("")

    return (i)
