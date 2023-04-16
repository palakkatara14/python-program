d={}
print("enter the number of elements=")
n=int(input())
for i in range(1,n+1):
    print("enter the key=")
    k=int(input())
    v=k*k
    
    print(v)
    d.update({k:v})
    print(d)

