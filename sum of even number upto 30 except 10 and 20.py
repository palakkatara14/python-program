sum = 0
for i in range(0,32,2):
    if i==10 or i==20:
        continue
    sum = sum+i
print(sum)