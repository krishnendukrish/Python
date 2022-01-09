str=input("enter the string:")
x=0
for i in range(len(str)):
 if(str[i]!=' '):
    x=x+1
print("the total number of characters in the string is ",x)