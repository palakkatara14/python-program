def prime_or_not(n):
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1 
    if count==2:
        print("prime")
    else:
        print("not prime")
n = int(input())
prime_or_not(n)