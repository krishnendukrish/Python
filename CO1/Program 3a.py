n=int(input("enter number of integers"))
num=[]
pos=[]
for i in range(n):
    num.append(int(input("enter the integers")))
    if num[i]>0:
        pos.append(num[i])
print(num)
print(pos)

