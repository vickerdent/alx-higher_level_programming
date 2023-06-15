#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        new_dict = {x: a_dictionary[x] for x in a_dictionary}
        for a in new_dict:
            new_dict[a] = new_dict[a] * 2
        return new_dict
