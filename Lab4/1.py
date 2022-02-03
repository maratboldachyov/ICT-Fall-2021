s = str(input())
t = int(input())

listS = list(s)
listS.pop(t)
s = "".join(listS)
print(s)