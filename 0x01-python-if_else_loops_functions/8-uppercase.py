#!/usr/bin/python3
def uppercase(str):
    result = ''
    for i in str:
        if (i == " "):
            result += " "
        elif (97 <= ord(i) <= 122):  # to change into uppercase
            result += chr(ord(i) - 32)  # ASCII ORDER 
        else:
            result += chr(ord(i))
    print("{}".format(result))
