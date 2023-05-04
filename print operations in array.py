import numpy as np 
m,n=list(map(int,input().split()))
m1=[]
m2=[]
for i in range(m):
    m1.append(list(map(int,input().split())))
for i in range(m):
    m2.append(list(map(int,input().split())))
a1=np.array(m1)
a2=np.array(m2)
print(np.add(a1,a2))
print(np.subtract(a1,a2))
print(np.multiply(a1,a2))
print(np.floor_divide(a1,a2))
print(np.mod(a1,a2))
print(np.power(a1,a2))