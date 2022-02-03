s = str(input())
cnt = 0
listS = list(s)

for i in range(len(listS)):
    if listS[i] == '.':
        listS[i] = ','
        cnt += 1
    s = "".join(listS)
print(s)
print("Number of commas is", cnt)