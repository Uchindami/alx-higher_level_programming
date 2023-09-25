#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ a safe_print_list function that prints the first x elements """
    counter = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            counter += 1
    except IndexError:
        pass

    print()

    return counter
