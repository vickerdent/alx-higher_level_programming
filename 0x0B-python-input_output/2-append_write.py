#!/usr/bin/python3
"""Defines a function that appends a string to a file"""

def append_write(filename="", text=""):
    """ Function that appends a string at the end of a
    text file and returns the number of characters added """
    
    if text and filename:
        with open(filename, "a") as f:
            f.write(text)
        return len(text)
