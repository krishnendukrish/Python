num=[]
n=int(input("enter a number"))
for i in range(n):
	num.append(int(input("enter number to insert")))
result=[x*x for x in num]
print(result)
