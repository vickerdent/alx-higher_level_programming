#!/usr/bin/python3
def print_last_digit(number):
    str_number = str(number)
    last_digit = str_number[-1]
    print(f"{last_digit}", end="")
    return int(last_digit)
