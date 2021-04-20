# Regular Expressions
import re


def check(str, s):
    if re.match(s, str):
        print("True")
    else:
        print("False")

    if re.search(s, str):
        print("True")
    else:
        print("False")
    print(re.findall(s, str))
    print(re.finditer(s, str))


if __name__ == '__main__':
    str = input("Enter a string pattern : ")
    s = input("Enter checking string : ")
    check(str, s)
