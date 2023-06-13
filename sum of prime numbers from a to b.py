n=int(input())
sum=0
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        sum=sum+i 
print(sum)