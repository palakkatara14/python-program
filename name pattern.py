n = int(input("enter n "))
c = 0
s = " VISHALJAISWAL!"
l = len(s)
for i in range(n):
    for j in range(i+1):
        print(s[c%l],end = " ")
        c+=1
    print()