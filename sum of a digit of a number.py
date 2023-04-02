n = int(input())
sum=0
for i in range(1,n+1):
    r = n%10
    sum = sum+r 
    n = n//10
print(sum)