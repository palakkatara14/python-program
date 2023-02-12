amount = int(input('enter amount'))
amount = amount-100
twok = amount//2000
amount = amount%2000
fiveh = amount//500
amount = amount%500
twoh = amount//200
amount = amount%200
oneh = amount//100+1
print('no. of 100 notes',oneh)
print('no. of 200 notes',twoh)
print('no. of 500 notes',fiveh)
print('no. of 2000 notes',twok)
