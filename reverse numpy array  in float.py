import numpy as np 
ls=list(map(int,input().split()))
arr=np.array(ls,dtype='float')
out=np.flip(arr)
print(out)