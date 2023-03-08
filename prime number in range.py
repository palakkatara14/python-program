n = int(input("enter n"))
for p in range(2,n+1):
    i=2
    for i in range(2,n):
        if p%i==0:
            i = n 
            break
    if i!=p:
        print(p,end = " ")