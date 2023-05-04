def hcf(a,b):
    i=1 
    while i<=a and i<=b:
        if a%i==0 and b%i==0:
            hcf=i 
        i=i+1 
    return hcf
a=int(input())
b=int(input())
c=hcf(a,b)
print(c)
        