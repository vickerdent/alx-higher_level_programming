#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    if len(sys.argv) < 2:
        print(sum)

    elif len(sys.argv) == 2:
        sum += int(sys.argv[1])
        print(sum)

    else:
        for arg in sys.argv:
            if arg == sys.argv[0]:
                continue
            sum += int(arg)
        print(sum)
