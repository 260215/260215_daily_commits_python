# Write a Python program to convert a list into a nested dictionary of keys
from array import *


def nested_dictionary(arr1, arr2):
    return [{a: b} for (a, b) in zip(arr1, arr2)]


if __name__ == '__main__':
    arr1 = [str(i) for i in input("Enter string values : ").split(' ')]
    arr2 = [int(i) for i in input("Enter integer values : ").split(' ')]
    print(nested_dictionary(arr1, arr2))

# Input
# arr1 = ["Monday" "Tuesday" "Wednesday" "Thursday"]
# arr2 = [1, 2, 3, 4]
