print("This program determines whether the student is allowed to sit in exam or not.")
print("Moreover the program prints the percentage of attendance")

print("Please, enter the number of classes held:")
n = int(input())

print("Please, enter the number of classes the student attended:")
m = int(input())

if m / n < 0.75:
      print("Not allowed")
elif m / n >= 0.75:
      print("Allowed")