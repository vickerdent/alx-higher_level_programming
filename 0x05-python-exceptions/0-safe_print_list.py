#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        while counter != x and counter < my_list[-1]:
            print(my_list[counter], end="")
            counter += 1
        print()
        return counter
    except:
        return counter
