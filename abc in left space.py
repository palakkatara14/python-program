n = int(input("enter n"))
for i in range(n):
    for j in range(n-i-1):
       print(' ',end = " ")
    for k in range(i+1):
        print(chr(65+i),end = " ")
    print()
