salary =  float(input("enter basic salary"))
if salary<=10000:
    gross = (20/100)*10000+(80/100)*10000+10000
    
    print(gross)
elif salary<=20000:
     gross  = (25/100)*20000+(90/100)*20000+20000
     print(gross)
elif salary>20000:
     gross  = (30/100)*20000+(95/100)*20000+20000
     print(gross)
else:
    print("nothing")
