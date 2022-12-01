#!/bin/usr/python3
def uppercase(str):
    result = ''
    for i in str:
        if (i == " "):
            result += " "
        elif (97 <= ord(i) < 122):
            result += chr(ord(i) - 32)
        else:
            result += chr(ord(i))
    print("{}".format(result))
