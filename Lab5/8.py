print("The program determines the senior and junior persons from a lot of 3 people")

print("Please, enter the age of first person:")
n = int(input())

print("Please, enter the age of second person:")
m = int(input())

print("Please, enter the age of third person:")
l = int(input())

if n > l and n > m:
    print("The oldest is", n)
    if l < m:
        print("The youngest is", l)
        exit()
    elif m < l:
        print("The youngest is", m)
        exit()
    else:
        print("The youngest two with age", l)
        exit()
if m > l and m > n:
    print("The oldest is ", m)
    if l < n:
        print("The youngest is", l)
        exit()
    elif n < l:
        print("The youngest is", n)
        exit()
    else:
        print("The youngest two with age", l)
        exit()
if l > n and l > m:
    print("The oldest is", l)
    if n < m:
        print("The youngest is", n)
        exit()
    elif m < n:
        print("The youngest is", m)
        exit()
    else:
        print("The youngest two persons with age", m)
        exit()