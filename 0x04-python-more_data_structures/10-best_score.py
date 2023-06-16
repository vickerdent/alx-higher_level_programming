#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary) > 0:
        prev = 0
        prev_key = ""
        curr = 0
        curr_key = ""
        big = 0
        big_key = ""
        for a in a_dictionary:
            curr = a_dictionary[a]
            curr_key = a
            if curr > prev:
                big = curr
                big_key = curr_key
                prev = curr
                prev_key = curr_key
            else:
                big = prev
                big_key = prev_key
        return big_key
    else:
        return None
