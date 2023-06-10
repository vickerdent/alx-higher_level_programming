#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    val = len(my_list) - 1
    while val >= 0:
        print("{:d}".format(my_list[val]))
        val -= 1
