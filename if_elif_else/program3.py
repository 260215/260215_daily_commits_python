# Write Python code that asks a user how many pizza slices they want.
# The pizzeria charges Rs 123.00 a slice. if user order even number of slices, price per slice is Rs 120.00.
# Print the total price depending on how many slices user orders.

def price_slice(slices):
    if slices % 2 == 0:
        print('{:.2f}'.format(slices * 120.00))
    else:
        print('{:.2f}'.format(slices * 123.00))


if __name__ == '__main__':
    slices = int(input("Enter the no. of slices : "))
    price_slice(slices)
