print("The program prints the Fibonacci sequence according to the range from 1 up to the nth number.")
fib1 = 0
fib2 = 1

n = int(input("Enter number of terms: "))

print("Fibonacci sequence:")

print(fib1, fib2, end=' ')

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
