print("This program determines your order and calculates you bill.")
print('Please, choose the appropriate size for your pizza. Available pizza sizes are: "S", "M" or "L".')
size = input()
while (size != "\"S\"" and size != "\"M\"" and size != "\"L\""):
	print('Error: Wrong pizza size. Available pizza sizes are: "S", "M" or "L".')
	print('Please, choose the appropriate size for your pizza once more:')
	size = input()

print('Do you wish pepperoni? Please, answer in "Y"(Yes) or "N"(No) format:')
pepperoni = input()
while(pepperoni != "\"Y\"" and pepperoni != "\"N\""):
	print ('Error: Wrong format of answer for pepperoni. Please, answer in "Y"(Yes) or "N"(No) format.')
	print('Please, print the appropriate option in right syntax format for pepperoni once more:')
	pepperoni = input()

print('Do you wish extra cheese? Please, answer in "Y"(Yes) or "N"(No) format:')
extra_cheese = input()
while (extra_cheese != "\"Y\"" and extra_cheese != "\"N\""):
	print('Error: Wrong format of answer for extra cheese. Please, answer in "Y"(Yes) or "N"(No) format.')
	print('Please, print the appropriate option in right syntax format for extra cheese once more:')
	extra_cheese = input()

bill = 0

if (size == "\"S\""):
	bill += 15
elif (size == "\"M\""):
	bill += 20
elif (size == "\"L\""):
	bill += 25

# Adding pepperoni
if (pepperoni == "\"Y\"" and size == "\"S\""):
	bill +=2 # +2 dollars on the total bill
elif (pepperoni == "\"Y\""):
	bill += 3

if (extra_cheese == "\"Y\""): 
	bill += 1

print("Your final bill is: ", bill, "$")