def perfect_or_not(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
           sum+=i
    if sum==n:
       print("perfect")
    else:
        print("not perfect")
n=int(input())
perfect_or_not(n)
        
    