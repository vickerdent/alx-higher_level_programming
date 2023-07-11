#!/usr/bin/python3
"""Student class"""

class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns student's serializable dict elements as a dict"""
        maindict = {}
        worlddict = self.__dict__
        for thing in worlddict:
            if type(worlddict[thing]) in [list, dict, str, int, bool]:
                maindict[thing] = worlddict[thing]
        return maindict