print("The program calculates the average of all numbers from 1 to a given number.")

n = int(input("Please, enter the number:"))

sum = 0

for i in range(n, 0, -1):
    sum += i
avg = sum / n
print("Sum of first 5 numbers is:", sum, "\n" "Average of 5 numbers is:", avg)
