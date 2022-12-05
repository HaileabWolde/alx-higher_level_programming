#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    n = len(sys.argv) - 1

    if (n != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    elif (sys.argv[2] != "+" and "-" and "*" and "/"):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    else:

        a = int(sys.argv[1])

        b = int(sys.argv[3])

        if (sys.argv[2] == "+" or "-" or "*" or "/"):

            for i in range(1, n+1):
                if (sys.argv[i] == "+"):
                    print("{} + {} = {}".format(a, b, add(a, b)))
                elif (sys.argv[i] == "-"):
                    print("{} - {} = {}".format(a, b, sub(a, b)))
                elif (sys.argv[i] == "*"):
                    print("{} * {} = {}".format(a, b, mul(a, b)))
                elif (sys.argv[i] == "/"):
                    print("{} / {} = {}".format(a, b, div(a, b)))
