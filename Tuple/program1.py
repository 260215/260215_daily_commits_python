# Write a Python program to find the repeated items of a tuple

def repeated_elements_tuple(arr):
    tup = tuple(arr)
    for i in tup:
        if tup.count(i) > 1:
            print(i, end=' ')


if __name__ == '__main__':
    arr = [int(i) for i in input("Enter elements : ").split(',')]
    repeated_elements_tuple(arr)

# Input : (1,3,4,32,1,1,1,31,32,12,21,2,3) input taken in the form of list and then converted into tuple
# Output: 1 3 32 1 1 1 32 3
