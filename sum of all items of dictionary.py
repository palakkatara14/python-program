d = {1:2,3:4}
print(sum(d.values()))
print(sum(d.keys()))
#another method 
d = {1:2,3:4,5:6}
sum =0
tot =0
for i in d:
    tot+=i
    sum = sum+d[i]
print(sum)
print(tot)