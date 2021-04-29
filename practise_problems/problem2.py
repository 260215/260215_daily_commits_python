# Write a program to remove the nth index character from a non-empty string

def remove_nth(s, n):
    return s[:n] + s[n + 1:]


if __name__ == '__main__':
    s = input("Enter a string : ")
    n = int(input("Enter the index : "))
    print("The expected result is : ", remove_nth(s, n))
