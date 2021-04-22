# Write a Python program to convert a list of tuples into a dictionary

def convert_to_dictionary(my_list):
    dic = dict()
    for day, num in my_list:
        dic.setdefault(day, num)
    print(dic)


if __name__ == '__main__':
    my_list = [("Sunday", 1), ("Monday", 2), ("Tuesday", 3), ("Wednesday", 4)]
    convert_to_dictionary(my_list)

# Output : {'Sunday': 1, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4}
