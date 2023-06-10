#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    prev = 0
    curr = 0
    big = 0
    for num in my_list:
        curr = num
        if curr > prev:
            big = curr
            prev = curr
        else:
            big = prev
    return big
