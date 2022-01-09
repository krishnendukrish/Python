a=int(input("enter number of words"))
k=[]
b=[]
i=1
while i<=a:
    n=input("enter the string")
    l=len(n)
    b.append(l)
    k.append(n)
    i=i+1
print(k)
print(max(b))



