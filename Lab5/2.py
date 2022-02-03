print("This program identifies whether the year is leap or not.")

print("Please, enter the value for year:")
n = int(input())

if (n % 400 == 0):
	print("The entered value is leap year")
elif (n % 100 == 0):
	print ("The entered value is not leap year")
elif (n % 4 == 0):
	print ("The entered value is leap year")
else:
	print ("The entered value is not leap year")