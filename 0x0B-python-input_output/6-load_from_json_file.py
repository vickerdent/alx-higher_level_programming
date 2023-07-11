#!/usr/bin/python3
"""Defines a function that writes an object to file"""
import json

def load_from_json_file(filename):
    """ Function that creates an Object from a “JSON file” """
    
    if filename:
        with open(filename, "r") as f:
            return json.load(f)
        