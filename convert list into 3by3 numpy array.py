import numpy as np 
ls=list(map(int,input().split()))
arr=np.array(ls)
out=arr.reshape(3,3)
print(out)