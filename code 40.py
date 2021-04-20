# Regular expression(search and replace)
import re


def replace(str, s):
    if re.search(s, str):
        print(re.sub(s, "00", str))
    else:
        raise print("Error!!!")


if __name__ == '__main__':
    str = input("Enter the string : ")
    s = input("Enter the pattern : ")
    replace(str, s)
