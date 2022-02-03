s = str(input().split())
n = int(input())
listS = list(s)

for i in range(len(listS)):
    if i <= n and listS[i] != '' and listS[i] != "":
        listS[i] = ""
m = "".join(listS)
print(m)



