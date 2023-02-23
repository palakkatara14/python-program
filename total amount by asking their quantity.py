tp = 0
ch = input("DO YOU WANT TO HAVE BURGER -50RS?(Y/N)")
if ch=='y'or ch=='Y':
    q = int(input("enter quantity: "))
    tp = tp+(50*q)
    
ch = input("DO YOU WANT TO HAVE PIZZA -150RS?(Y/N)")
if ch=='y'or ch=='Y':
    q = int(input("enter quantity: "))
    tp = tp+(150*q) 

ch = input("DO YOU WANT TO HAVE FRENCH FRIES -100RS?(Y/N)")
if ch=='y'or ch=='Y':
    q = int(input("enter quantity: "))
    tp = tp+(100*q)
    
ch = input("DO YOU WANT TO HAVE COKE -30RS?(Y/N)")
if ch=='y'or ch=='Y':
    q = int(input("enter quantity: "))
    
    tp = tp+(30*q) 
    
ch = input("DO YOU WANT TO HAVE PANIPURI -50RS?(Y/N)")
if ch=='y'or ch=='Y':
    q = int(input("enter quantity: "))
    tp = tp+(50*q)
    
print(tp)

