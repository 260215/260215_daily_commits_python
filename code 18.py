# Functions
def hello(word):
    print(word * 3, end='\n')


if __name__ == '__main__':
    word = input("Enter a word : ")
    hello(word)
    func = hello
    print(func(word))