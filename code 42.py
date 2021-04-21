# More on Character classes
import re


def check():
    pattern = r"[A-Z][a-z][0-9]"
    if re.search(pattern, "L1x"):
        print("Matched 1")
    if re.search(pattern, "Xt8"):
        print("Matched 2")


if __name__ == '__main__':
    check()
