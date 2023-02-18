from math import sqrt
centre = int(input("enter number"))
radius = int(input("enter number"))
x1 = int(input("enter number"))
x2 = int(input("enter number"))
y1 = int(input("enter number"))
y2 = int(input("enter number"))
x = (x2-x1)*(x2-x1)
y = (y2-y1)*(y2-y1)

d = sqrt(x+y)
if d < radius:
    print("inside the circle")
elif d > radius:
    print("outside the circle")
else:
    print("on the circle")