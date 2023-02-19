a = int(input("enter number"))
if a%2==0:
    print("even")
else:
    print("odd")
    if a%2!=0:
        b = int(input("enter number"))
    for i in range(1 ,5 ,1):
         print(i,end ="#")