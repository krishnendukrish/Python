clr1=["red","blue","green"]
clr2=["blue","yellow"]
print(clr1)
print(clr2)
for i in range(len(clr1)):
    if clr1[i] not in clr2:
        print("the color is :",clr1[i])