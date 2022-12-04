#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    n = len(sys.argv) - 1

    if (n == 0):
        print(sum)

    else:
        for i in range(1, n+1):
            sum += int(sys.argv[i])
        print(sum)
