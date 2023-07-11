#!/usr/bin/python3
"""Defines a function that writes an object to file"""
import json

def save_to_json_file(my_obj, filename):
    """ Function that writes an Object to a text file,
    using a JSON representation: """
    
    if my_obj and filename:
        with open(filename, "w") as f:
            json.dump(my_obj, f)
