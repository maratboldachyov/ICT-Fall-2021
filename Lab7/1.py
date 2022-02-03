n = int(input("Please, enter the integer and up to this index the program would remove the characters:"))
s = input("Please, enter the string:")
for i in range(0, n):
    if not 'a' <= s[i] and 'z' >= s[i]:
        continue
    else:
        print(s[i], end = '')
for i in range(n, len(s)):
    print(s[i], end = '')