n = int(input())
rev=0
i=1
for i in range(1,n+1):
    while(n!=0):
        r = n%10
        rev = rev*10+r 
        n = n//10
print(rev)