# Write a python program to check if the input number is
# -real number
# -float number
# -string-complex number
# -Zero (0)
import re

def check(num):
    if re.match(r'^-?\d+(?:\.\d+)$', num):
        print("The number is a float number.")
    if num.isnumeric():
        print("The number entered is a real number.")
    elif num == "0":
        print("The number entered is Zero(0).")
    else:
        print("The number entered is a complex number.")


if __name__ == '__main__':
    num = (input("Enter a number : "))
    check(num)

