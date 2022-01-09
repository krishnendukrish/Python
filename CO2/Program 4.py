import math
a=int(input("enter starting 4 digit number"))
b=int(input("enter ending 4 digit number") )
x=[]
for i in range(a,b):
      count=0
      num=i
      while num>0:
         d=num%10
         if d not in [0,2,4,6,8]:
              count=1
              break
         num=int(num/10)
      if count==0 and math.sqrt(i) % 1==0:
              x.append(i)
print("the list of perfect square numbers are:",x)
      
