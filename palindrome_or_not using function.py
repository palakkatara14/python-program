import math 
def palindrome_or_not(n):
    k=n 
    t=0
    while n>0:
        r=n%10
        n=n//10
        t=t*10+r
    if k==t:
        print("palindrome")
    else:
        print("not palindrome")
n=int(input())
palindrome_or_not(n)