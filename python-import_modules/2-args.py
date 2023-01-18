#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    if len(sys.argv) - 1 == 0:
        print("{} arguments.".format(len(sys.argv) - 1))
    else:
        if len(sys.argv) - 1 == 1:
            print("{} argument:".format(len(sys.argv) - 1))
        else:
            print("{} arguments.".format(len(sys.argv) - 1))
    if len(sys.argv) != 0:
        for index in range(1, len(sys.argv)):
            print("{}: {}".format(index, sys.argv[index]))
