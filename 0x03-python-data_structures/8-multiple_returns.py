#!/usr/bin/python3
def multiple_returns(sentence):
    total = len(sentence)
    first_letter = sentence[0]
    if total == 0:
        return None
    return total, first_letter
