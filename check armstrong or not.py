n = int(input("enter number"))
k = n 
t = 0
while n!=0:
      r = n%10
      n = n//10 
      t = t+r**3
if k==t:
    print("armstrong")
else:
    print("not armstrong")