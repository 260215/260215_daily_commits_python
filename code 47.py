# ASCII Codes

arr = ['A', 'V', ' ', '@']
brr = []
for i in arr:
    brr.extend(ord(j) for j in i)
print(list(brr))

s = "SuVaM"
print([ord(j) for j in s])