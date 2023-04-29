import random
print("*****WELCOME EVERYONE!*******")

n = random.randint(1,10)
att=3
while att:
    guess=int(input("enter the choice you want to guess"))
    if guess<n:
        print("TOO LOW !")
        
    elif guess>n:
        print("TOO HIGH !")
        
    else:
        print("**😀😀 CONGRATULATIONS😀😀 !** ,YOU WON THE GAME")
    att-=1
        
else:
    print("😔😔 YOU LOSE THE GAME😔😔 ! ,BETTER LUCK NEXT TIME")
