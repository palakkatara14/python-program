import random
n=random.random()
print(n)
w=int(input("enter the width"))
otp=str(n)[-w:]
print("your one time password is")
print(otp)