print("The program accepts the rows number from a user and prints the reverse number pattern using a loop.")

n = int(input("Enter the rows number: "))

print("Output:")

while n > 0:
    i = n
    for i in range(n, 0, -1):
        print(i, end = ' ')
    print("\n")
    n -= 1
