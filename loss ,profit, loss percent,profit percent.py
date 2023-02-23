cp = int(input("enter number "))
sp = int(input("enter number "))
if sp>=cp:
   profit = sp-cp
   per = (profit/cp)*100
   print("profit")
   print("%0.2f"%per,end = '%')
else:
    loss = cp-sp
    per = (loss/cp)*100
    print("loss")
    print("%0.2f"%per,end = '%')