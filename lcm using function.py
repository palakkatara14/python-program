def lcm(a,b):  
    # selecting the greater number  
    if a > b:  
        min = a  
    else:  
        min = b  
    while 1:  
        if min%a==0 and min%b==0: 
            lcm = min  
            break  
        min += 1  
    return lcm    
a=int(input())
b=int(input())
out=lcm(a,b)
print(out)