#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is not None and key is not None:
        if key in a_dictionary:
            a_dictionary.pop(key)
        return a_dictionary
