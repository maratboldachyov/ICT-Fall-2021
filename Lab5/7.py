print("The program calculates your grade according to your current points")

print("Please, enter your the amount of your points for the discipline to calculate your grade:")
a = int(input())

if a < 25:
    print("F")
elif a >= 25 and a < 45:
    print("E")
elif a >= 45 and a < 50:
    print("D")
elif a >= 50 and a < 60:
    print("C")
elif a >= 60 and a < 80:
    print("B")
elif a >= 80:
    print("A")
