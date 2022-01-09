a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if a>b:
    if a>c:
       print(a,"is big")
    else:
       print(c, "is big")
elif b>c:
    print(b, "is big")
else:
    print(c, "is big")