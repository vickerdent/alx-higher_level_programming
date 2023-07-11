#!/usr/bin/python3
"""Student class"""

class Student:
    """Student class"""

    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age

    def to_json(self, attrs=None):
        """Returns student's serializable dict elements as a dict"""
        filterattr = 0
        if type(attrs) == list:
            filterattr = 1
            for x in attrs:
                if type(x) is not str:
                    filterattr = 0
                    break
        maindict = {}
        worlddict = self.__dict__
        for thing in worlddict:
            if type(worlddict[thing]) in [list, dict, str, int, bool]:
                if filterattr == 0 or thing in attrs:
                    maindict[thing] = worlddict[thing]
        return maindict