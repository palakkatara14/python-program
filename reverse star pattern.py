n = int(input("enter n"))
for i in range(n):
    for j in range(i):
       print(' ',end = " ")
    for k in range(n-i):
        print("*",end = " ")
    print()
