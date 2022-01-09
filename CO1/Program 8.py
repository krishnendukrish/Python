str=input("enter a string")
len=len(str)
k=list(str)
a=str[0]
i=1
while i<len:
    if a==k[i]:
        k[i]="$"
    i=i+1
st="".join(k)
print(st)

