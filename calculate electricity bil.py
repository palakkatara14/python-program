unit =  int(input("enter units of electricity bill"))
if unit<=50:
    bill = unit*0.50
elif unit>50 and unit<=150:
     bill = unit*0.50+(unit-50)*0.75
elif unit>150 and unit<=250:
     bill = bill*0.50+100*0.75+(unit-150)*1.25
elif unit>=250:
     bill = bill*0.50+100*0.75+100*1.25+(unit-250)*1.50
bill = bill+bill*0.20
print(bill)