#!/usr/bin/python3
"""Defines a function that returns a class's
serializable dict elements"""

def class_to_json(obj):
    """Returns a class's serializable dict 
    elements as a dict"""
    maindict = {}
    worlddict = obj.__dict__
    for thing in worlddict:
        if type(worlddict[thing]) in [list, dict, str, int, bool]:
            maindict[thing] = worlddict[thing]
    return maindict