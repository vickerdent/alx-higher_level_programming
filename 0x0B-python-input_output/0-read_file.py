#!/usr/bin/python3
"""Defines a function that prints a UTF-8 text file"""

def read_file(filename=""):
    """ Function that prints a file's contents """

    if filename:
        with open(filename, "r") as f:
            print(f.read(), end="")
