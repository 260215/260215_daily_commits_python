# Write a program to get a string from a given string where all occurrences of its first character
# have been changed to '$' except for the first character itself
# Sample string : restart
# Expected string : resta$t

def get_string(s):
    c = s[0]
    s = s.replace(c, '$')
    s = c + s[1:]

    return s


if __name__ == '__main__':
    s = input("Enter a string : ")
    print("The expected output string is : ", get_string(s))
