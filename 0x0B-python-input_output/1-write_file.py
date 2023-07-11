#!/usr/bin/python3
"""Defines a function that writes a string to a file"""

def write_file(filename="", text=""):
    """ Function that writes a string to a text file
    and returns the number of characters written """
    
    if text and filename:
        with open(filename, "w") as f:
            f.write(text)
        return len(text)
