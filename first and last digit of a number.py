n = int(input("enter  n "))
last = n%10
while n>=10:
    n = n//10
first = n
print(first,last)