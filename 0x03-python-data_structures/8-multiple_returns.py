#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None or len(sentence) == 0:
        return (0, None)
    total = len(sentence)
    first_letter = sentence[0]
    return total, first_letter
