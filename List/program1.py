# Write a Python program to find the second smallest number in a list

def second_smallest(num_list):
    num_list.sort()
    print("The second smallest number in a list is : ", num_list[1])


if __name__ == '__main__':
    num_list = [int(i) for i in input("Enter numbers : ").split(' ')]
    second_smallest(num_list)

# Input : [4, 9, 7, 2, 8]
# Output : 4
