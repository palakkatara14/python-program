import numpy as np 
ls=list(map(int,input().split()))
arr=np.array(ls)
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))