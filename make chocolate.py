small =  int(input("enter no . of small bars"))
big =  int(input("enter no . of big bars"))
goal  =  int(input("enter no . of goals"))
if ((small  + big * 5) < goal): 
  print("it can be done")
 
else:
    print("it can not be done")
    print("-1")