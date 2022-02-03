print("This program identifies whether the last digit of number is divisible by 3 or not.")

print("Please, enter the number:")
n = int(input())

if n % 10 % 3 == 0:
    print("Yes")
else:
    print("No")