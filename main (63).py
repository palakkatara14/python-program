n = int(input("enter number"))  
k = n
t = 0
while n>0:
    r = n%10
    n = n//10
    t = t*10+r 
if k == t:
    print("pallindrom")
else:
    print("not pallindrom")