a=(input("enter some words seperated with comma"))
b=a.split(",")
long=len(b[1])
for i in b:
    if long<len(i):
       long=len(i)
print("length of longest word is", long)



