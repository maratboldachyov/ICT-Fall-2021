n = int(input("Please, enter the number up to that would be deleted characters:"))
s = str(input("Please, enter your string:"))

for i in range(len(s)):
    if(s.isalpha()):
        print(s)
        break
