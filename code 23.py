nums = [int(i) for i in input("Enter elements : ").split(' ')]
print(list(filter(lambda z: z % 2 == 0, nums)))
