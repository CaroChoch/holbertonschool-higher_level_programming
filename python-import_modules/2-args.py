#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    argv_count = len(argv) - 1

    if argv_count == 0:
        print("{:d} arguments.".format(argv_count))
    elif argv_count == 1:
        print("{:d} argument:".format(argv_count))
    else:
        print("{:d} arguments.".format(argv_count))
    for index in range(1, argv_count + 1):
        print("{:d}: {:s}".format(index, sys.argv[index]))
