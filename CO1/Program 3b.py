num=[]
n=int(input("enter number of elements you want to insert"))
for i in range(n):
	num.append(int(input("enter element to insert")))
result=[x*x for x in num]
print(result)
