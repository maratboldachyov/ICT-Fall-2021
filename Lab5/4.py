print("This program determines whether the employee has an opportunity to have a net bonus. "
	  "If the employee has an experience over 5 years, employee can account on it.")

print("Please, enter your salary:")
salary = float(input())

print ("Please, enter your year of service:")
experience = float(input())

bonus = 0

if (experience >= 5.0):
	bonus = salary * 0.05

print("Net bonus = ", bonus)