#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        for i in sorted(a_dictionary, key=lambda x: x):
            print("{}: {}".format(i, a_dictionary[i]))
