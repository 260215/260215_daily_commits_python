from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))

a={1, 2}
print(len(list(product(range(3), a))))