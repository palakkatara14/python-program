import random
ls =['rock','paper','scissor']
c_c= random.choice(ls)
u_c=input("enter the choice")

if u_c=='rock'and c_c=='scissor' or u_c=='paper'and c_c=='rock' or u_c=='scissor'and c_c=='paper':
    print("😃😃USER WINS😃😃")
    
else:
    print("😃😃COMPUTER WINS😃😃")
    
    