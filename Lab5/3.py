print("This program determines the Body Mass Index(BMI) and shows the interpretation of the index.")

print("Please, enter your weight:")
weight = float(input())

print("Please, enter your height:")
height = float(input())

bmi = weight / (height * height)

if (bmi < 18.5):
	print ("Your BMI is", round(bmi), ", you are underweight")
elif (bmi < 25.0):
	print ("You BMI is", round(bmi), ", you have a normal weight")
elif (bmi < 30.0):
	print ("Your BMI is", round(bmi), ", you are slightly overweight")
elif (bmi  < 35.0):
	print ("Your BMI is", round(bmi), ", you are obese")
else:
	print ("Your BMI is", round(bmi), ", you are clinically obese")