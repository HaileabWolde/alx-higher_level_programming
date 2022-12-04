#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1  # counting the arguments
    if (n == 0):
        print("{} arguments.".format(n))
    else:
        print("{} arguments:".format(n))
        for i in range(1, n+1):  # parsing through the command line arguments
            print("{}: {}".format(i, sys.argv[i]))
