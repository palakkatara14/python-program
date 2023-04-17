#sorted in ascending
d = {'krishna':1000,'radhika':200}
val = sorted(d.values())

out = {}
for i in val:
    for j in d:
        if d[j]==i:
           out[j]=i
           d.pop(j)
           break 
print(out)
#sorted in descending
d = {'krishna':1000,'radhika':200}
val = sorted(d.values())
val=val[::-1]
out = {}
for i in val:
    for j in d:
        if d[j]==i:
           out[j]=i
           d.pop(j)
           break 
print(out)