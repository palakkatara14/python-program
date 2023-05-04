import math 
def strong_or_not(n):
    k=n 
    t=0
    while n:
        r=n%10
        t=t+math.factorial(r)
        n=n//10
    if k==t:
        print("strong")
    else:
        print("not strong")
n=int(input())
strong_or_not(n)