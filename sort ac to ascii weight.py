ls = ['rishabh','yatin','abhishek']
ls.sort(key = lambda x : sum(map(ord,x)))
print(ls)