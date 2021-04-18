file = open("my_file.txt", "r+")
print(file.read())
print(file.read(16))
file.close()