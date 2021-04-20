# Regular Expressions
import re


def check(str, s):
    if re.match(s, str):
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    str = input("Enter a string pattern : ")
    s = input("Enter checking string : ")
    check(str, s)
