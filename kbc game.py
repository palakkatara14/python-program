print('''Let\'s play kbc.
To deviyo or sajjano shuru krte h kaun banega crorepati beth jaeye hotseat pr !\n
Pehla sawal aapki computer screens par ye rha-''')
ques=['Q1- kya aap engineering kr rhe h?' , 'Q2- aap engineering kyu kr rhe h?' , 'Q3- aapko engineering krke kesa lg rha h?' , 'Q4-aapko kya lgta h aapko job milegi?' , 'Q5-aapki sbse psndida bhasha konsi h?' , 'Q6-apni python faculty ke prati bhavnaye chuniye.' , 'Q7-rate your 1st sem ki faculty.']
opt=[['a:lag to esa hi rha h','b:nhi','c:hme nhi pta','d:aapko kya lgta h?'] , ['a:trending h','b:paisa kamane ke liye','c:ghrwalo ne kha tha','d:fhaltu sawal mt pucho'],['a:jale pe namak mt chidko','b:maut aa rhi h','c:thik  thak','d:hme ni pta'],['a:milegi kese nhi','b:ghanta milegi','c:mujhe to rona aa rha h','d:apna time aaega'],['a:hai ich nhi','b:C','c:python','d:are yo ka puch liyo'],['a:raddadh','b:smjh jao','c:no comments','d:mara zindagi safal hogiya'],['a:150 rupiya lega','b:10 clole(crore)','c:-10','d:super se bhi uper']]
ans=[opt[0][0][0],opt[1][2][0],opt[2][1][0],opt[3][3][0],opt[4][3][0],opt[5][1][0],opt[6][1][0]]
score=0
f=0
for i in range(7):
     print(ques[i])
     print('options ye rhe aapke computer screens par-\n',opt[i])
     x=input('\napna uttar likhiye = ')
     if x==ans[i]:
         score=score+5000*2*(i+1)
         print('\nmubarak ho! aap jeet gye h {} rupay'.format(score))
         print('\nAgla sawal aapki computer screens par ye rha-'if i<6 else'')
     else:
          f=1
          break

if f==1:
     print('\naww! so sad... bade hi dukh ke sath suchit kiya jata h ki aapke lag gye h or aap {} dhanrashi apne sath apne ghr le ja skte h\nDhanyavaad!'.format(score))
else:
     print('congratulations!\nAap jeet gaye h {} rupay\nGame khelne ke liye bhot bhot shukriya.'.format(score))