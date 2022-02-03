print("The program prints the sequence of prime numbers in the certain range.")

n = int(input("Enter starting number: "))
m = int(input("Enter ending number: "))

print("Prime numbers between", n, "and", m, "are:")

for i in range(n, m + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            print(i)
