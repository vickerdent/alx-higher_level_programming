#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0 or sentence is None:
        return None
    total = len(sentence)
    first_letter = sentence[0]
    return total, first_letter
