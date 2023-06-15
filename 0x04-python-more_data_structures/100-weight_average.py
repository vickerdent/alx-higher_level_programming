#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        if my_list == []:
            return 0
        numerator = 0
        denominator = 0
        for score, weight in my_list:
            numerator += score * weight
            denominator += weight
        return numerator / denominator
