#!/usr/bin/python3


if __name__ == "__main__":
    import sys

    no = len(sys.argv) - 1
    if no == 0:
        print("0 arguments.")
    elif no == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(no))
    for i in range(no):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
