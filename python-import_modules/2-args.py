#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv_count = len(sys.argv) - 1

    if argv_count == 0:
        print("{} arguments.".format(argv_count))
    elif argv_count == 1:
        print("{} argument:".format(argv_count))
    else:
        print("{} arguments.".format(argv_count))
    for index in range(argv_count):
        print("{}: {}".format(index + 1, sys.argv[index + 1]))
