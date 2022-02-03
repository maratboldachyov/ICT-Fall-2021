print("The program prints only those numbers from the given list that"
      "satisfy the following conditions:", "\n"
      "● The number must be divisible by 3;", "\n"
      "● If the number is greater than 120, then skip it and move to the next number;", "\n"
      "● If the number is greater than 300, then stop the loop.")

list1 = [12, 75, 151, 108, 147, 324, 30]
print("Given list is:", list1)

print("Output:")

for i in range(len(list1)):
    if list1[i] % 3 == 0 and list1[i] < 120:
        print(list1[i])
    elif list1[i] > 300:
        break
