def calculator(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a//b 
    return c,d,e,f 
a = int(input())
b = int(input())
out= calculator(a,b)
print(out)