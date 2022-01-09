n=int(input("enter number of list elements"))
over=[]
for i in range(n):
    over.append(int(input("enter element")))
    if over[i]>100:
       over[i]="over"
print(over)

