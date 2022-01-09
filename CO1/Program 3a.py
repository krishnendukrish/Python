n=int(input("enter number of integers you want to enter"))
num=[]
pos=[]
for i in range(n):
    num.append(int(input("enter the integers")))
print(num)
for i in num:
    if i>0:
        pos.append(i)
print(pos)

