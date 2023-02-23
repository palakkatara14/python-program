a = int(input("enter marks of first : "))
b = int(input("enter marks of second : "))
c = int(input("enter marks of third : "))
d = int(input("enter marks of fourth : "))
e = int(input("enter marks of fifth : "))
total = a+b+c+d+e
p = (total)//5
if p>=90:
    grade="A+"
elif p>=80 and p<=90:
    grade="A"
elif p>=70 and p<=80:
    grade="B+"
elif p>=60 and p<=70:
    grade="B"
elif p>=50 and p<=60:
    grade="C"
else:
    grade="FAIL"
print(total)
print(p)
print(grade)