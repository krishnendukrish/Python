vowel=["a","e","i","o","u"]
name=[]
n=int(input("enter number of names"))
for i in range(n):
	name.append(input("name:"))
for i in name:
	print(i,"have",end=" ")
	for j in vowel:
		for v in i:
			if j==v:
                           print(v,end=" ")
			    	       










