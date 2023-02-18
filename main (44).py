a = int(input("enter number"))
b = int(input("enter number"))
c = int(input("enter number"))
d = a+b+c==180
out = 'right  angle triangle'*d + 'not right triangle'*(1-d)
print(out)
