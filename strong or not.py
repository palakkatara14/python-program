import math
num = int(input("enter number: "))
temp = num 
sum = 0
while num:
     r = num%10 
     sum = sum + math.factorial(r)
     num = num//10
if sum==temp:
    print("strong")
else:
    print("not strong")