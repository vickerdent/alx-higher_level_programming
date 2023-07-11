#!/usr/bin/python3
"""Defines a function that loads an object from a json string"""
import json

def from_json_string(my_str):
    """ Function that returns an object (Python data 
    structure) represented by a JSON string """
    
    if my_str:
        return json.loads(my_str)
