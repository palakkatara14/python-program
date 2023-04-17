d1 = {'a':100,'b':200,'c':300}
d2 = {'a':200,'b':200,'d':400}
out = d1.copy()
for i in d2:
    if i in out:
        out[i]=out[i]+d2[i]
    else:
        out[i]=d2[i]
print(out)
