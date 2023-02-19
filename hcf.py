a = int(input("enter number"))
b = int(input("enter number"))
i = 1 
while i<=a and i<=b:
    if a%i==0 and b%i==0:
        hcf = i 
    i = i+1 
print(hcf)

       