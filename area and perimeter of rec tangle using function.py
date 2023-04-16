def area_p(l,b):
    a=l*b 
    c = 2*(l+b)
    return (a,c)
l = int(input())
b = int(input())
d=area_p(l,b)
print(d)