import numpy as np 
m,n=list(map(int,input().split()))
ls=[]

for i in range(m):
    ls.append(list(map(int,input().split())))
arr=np.array(ls)
print(arr.T)
print(arr.flatten())