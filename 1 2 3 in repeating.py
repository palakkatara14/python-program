n = int(input(" "))
count = 1
for i in range(1,n+1):
    for j in range(i):
       print(count,end = " ")
       count = count + 1 
       if count >9:
           count = 1
    print()