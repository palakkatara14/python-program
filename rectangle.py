n = int(input())
for i in range(n):
    
    if i==0 or i==n-1:
        print('*'*13)
    elif i==1:
        print(' '*13)
    else:
        print('*'+' '*11+'*')
    