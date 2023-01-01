#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    function divides element by element 2 lists.
    my_list_1 and my_list_2 can contain any type
    (integer, string, etc.)
    list_length can be bigger than the length of both lists
    Returns a new list (length = list_length) with all
    divisions
    If 2 elements can’t be divided, the division result
    should be equal to 0
    """
    new_list = []

    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]

        except (TypeError, ValueError):
            div = 0
            print("wrong type")

        except ZeroDivisionError:
            div = 0
            print("division by 0")

        except IndexError:
            div = 0
            print("out of range")

        finally:
            new_list.append(div)

    return (new_list)
