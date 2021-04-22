# Write a Python program to change the position of every n-th value with the (n+1)th in a list

def change_position(my_list):
    if len(my_list) % 2 == 0:
        for i in range(0, len(my_list), 2):
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        return my_list
    else:
        for i in range(0, len(my_list) - 1, 2):
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        return my_list


if __name__ == '__main__':
    my_list = [int(i) for i in input("Enter elements : ").split(' ')]
    print(change_position(my_list))
