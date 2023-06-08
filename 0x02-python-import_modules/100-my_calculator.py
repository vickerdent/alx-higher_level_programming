#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] not in ["+", "-", "*", "/"]:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        if sys.argv[2] == "+":
            print(a, sys.argv[2], b, "=", add(a, b))
        if sys.argv[2] == "-":
            print(a, sys.argv[2], b, "=", sub(a, b))
        if sys.argv[2] == "*":
            print(a, sys.argv[2], b, "=", mul(a, b))
        if sys.argv[2] == "/":
            print(a, sys.argv[2], b, "=", div(a, b))

    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
