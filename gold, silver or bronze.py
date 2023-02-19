amount = int (input ("enter number"))
if amount > 25000:
   print ("category is gold")
   discount = (20/100) * amount 
   amount = amount - discount
   print(amount)
elif amount >= 10000 and amount <= 25000:
     print ("category is silver")
     discount = (10/100) * amount
     amount = amount - discount 
     print(amount)
    
   
else:
    print ("category is bronze")
    discount = (5/100) * amount 
    amount = amount - discount
    print(amount)
print("thank you") 
print("visit again")
print("fuck you agr psnd na aaye toh")
