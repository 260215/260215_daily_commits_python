# Write a Python program to find maximum and the minimum value in a set

def max_and_min(my_list):
    print("The maximum value in the set is : ", max(set(my_list)))
    print("The minimum value in the set is : ", min(set(my_list)))


if __name__ == '__main__':
    my_list = [int(i) for i in input("Enter elements : ").split(' ')]
    max_and_min(my_list)

# Input : [8, 16, 24, 1, 25, 3, 10, 65, 55]
# Output : maximum=65, minimum=1
