ls = [1,2,3,4,4,5]
d = {}
for i in ls:
    if i in d:
        d[i]=d[i]+1 
    else:
        d[i] = 1 
for i in d.keys():
    if d[i]>=1:
        print(d[i])