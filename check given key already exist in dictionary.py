
d = {}
print("enter elements")
n = int(input())

for i in range(n):
    print("enter keys",end=" ")
    k = input()
    print("enter values",end=" ")
    v = (input())
    d.update({k:v})
    print(d)
z=input("enter a key")

if z in d:
    print("exist")
else:
    print("not exist")
    