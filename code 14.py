# for loop more
arr = [1, 2, 3, 4, 5]
sum = 0
for i in range(len(arr)):
    sum += arr[i]
print(sum)

sum1 = 0
for i in range(0, len(arr), 2):
    sum1 += arr[i]
print(sum1)

for num in range(10):
    print(num, end=' ')