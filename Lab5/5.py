print("The program identifies whether the entered parameters correspond to square of rectangle")

print("Please enter the length of the shape:")
n = int(input())

print("Please enter the width of the shape:")
m = int(input())

if n == m:
    print("The presented shape is a square with a length and width equal to", n)
elif n > m:
    print("The presented shape is a rectangle with a length", n, "and width", m)
elif m > n:
    print("The presented shape is a rectangle with a length", m, "and width", n)