for i in range(100,1000):
    n = i
    t = 0 
    while n!=0:
          r = n%10 
          n = n//10 
          t = t+r**3
    if t==i:
        print(i)