#!/usr/bin/python3
import sys

def main():
    if len(sys.argv) < 2:
        print("0 arguments.")

    elif len(sys.argv) == 2:
        print("1 argument:")
        print("1:", sys.argv[1])

    else:
        print(len(sys.argv) - 1, "arguments:")
        for index, arg in enumerate(sys.argv):
            if arg == sys.argv[0]:
                continue
            print(index, ": ", arg, sep="")

if __name__ == "__main__":
    main()
