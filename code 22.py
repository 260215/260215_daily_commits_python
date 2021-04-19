arr = [1, 2, 3, 4, 5]
print(list(map(lambda x: x + 5, arr)))

nums = [int(i) for i in input("Enter elements : ").split(' ')]
print(list(map(lambda y: y ** 3, nums)))
