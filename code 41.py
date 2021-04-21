# Regular Expressions(Character Class)
import re


def check():
    # pattern = r"[aeiou]"
    if re.search(r"[aeiou]", "grey"):
        print("Matched 1")
    if re.search(r"[aeiou]", "qwertyuiop"):
        print("Matched 2")
    if re.search(r"[aeiou]", "rhythm myths"):
        print("Matched 3")


if __name__ == '__main__':
    check()
