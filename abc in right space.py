n = int(input("enter n"))
for i in range(n):
    for j in range(i+1):
       print(chr(65+j),end = " ")
    print()
