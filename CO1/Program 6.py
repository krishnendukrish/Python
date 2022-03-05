n=int(input("enter number of names"))
names=[]
for i in range(n):
    names.append(input("enter name"))
s=0
for x in names:
    b=x.count("a")
    s=s+b
print(s)
