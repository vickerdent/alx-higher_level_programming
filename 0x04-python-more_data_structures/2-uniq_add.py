#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniquers = []
    sum = 0
    if my_list is not None:
        for i in my_list:
            if i not in uniquers:
                sum += i
                uniquers.append(i)
        return sum
    else:
        return None
