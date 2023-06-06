#!/usr/bin/python3
def uppercase(str):
    final = ""
    for c in str:
        if ord(c) in range(97, 123):
            final += chr(ord(c) - 32)
        else:
            final += c
    print(f"{final}")
