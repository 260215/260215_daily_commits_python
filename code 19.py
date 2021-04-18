# modules
import math


def func(num):
    return int(math.sqrt(num))


def fun(num):
    return math.sqrt(num)


if __name__ == '__main__':
    num = int(input("Enter a number : "))
    print(func(num))
    print("{:.2f}".format(fun(num)))
