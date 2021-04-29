# Write a program to find the first repeated character in a given string


def first_repeated(s):
    for i, c in enumerate(s):
        if s[:i + 1].count(c) > 1:
            return c

    return "None"


if __name__ == '__main__':
    s = input("Enter a string : ")
    print("The first repeated character is : ", first_repeated(s))

# Input : abcdabcd
# Output : a
