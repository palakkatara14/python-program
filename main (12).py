p = float(input('enter principal'))
r = float(input('enter rate'))
t = float(input('enter time'))
n = float(input('enter n'))
k = (1+r/100)
ci = p*pow(k,n*t)
A  = p+ci
print(ci)
print(A)