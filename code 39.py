# Regular Expressions
import re


def check(str, s):
    match = re.search(s, str)
    if match:
        print(match.group())
        print(match.start())
        print(match.end())
        print(match.span())


if __name__ == '__main__':
    str = input("Enter a string pattern : ")
    s = input("Enter checking string : ")
    check(str, s)
