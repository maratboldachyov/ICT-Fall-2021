n = int(input("Please, enter your age:"))
s = str(input("Please, enter your sex in M or F format:"))
m = str(input("Please, enter your marital status in Y or N format:"))

if s == 'F':
    print("Your place of service is  only URBAN AREA")
if s == 'M':
    if n >= 20 and n < 40:
        print("You don't have any restrictions. You can work ANYWHERE")
    elif n >= 40 and n < 60:
        print("Your place of service is only URBAN AREA")
    else:
        print("ERROR")
