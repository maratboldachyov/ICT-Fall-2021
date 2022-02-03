print("Please, enter the amount of purchased quantity:")
n = int(input())

if n * 100 >= 1000:
    print("You get a 10% discount with total cost of your order:")
    print(n * 100 - 10 * n)
else:
    print("Unfortunately, you don't get any discount. The total cost of your order:")
    print(n * 100)