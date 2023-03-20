str = input()
vowel = "aeiou"
digit = "1234567890"
consonant = "bcdfghjklmnpqrstvwxyz"
ws = " "
v = 0
c = 0
d = 0
w = 0
for i in str:
    if i in vowel:
         v = v+1
    elif i in digit:
         d = d+1
    elif i in consonant:
          c = c+1
    elif i in ws:
           w = w+1
print(v)
print(d)
print(c)
print(w)



