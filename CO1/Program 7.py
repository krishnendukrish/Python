n1 = int(input("number of integers in first list "))
list1 = []
for i in range(n1):
    list1.append(int(input("enter integers in list1")))
n2 = int(input("number of integers in second list "))
list2 = []
for j in range(n2):
    list2.append(int(input("enter integers in list2")))
both = []
if n1 == n2:
    print("The lists are in same length")
else:
    print("The lists are not in same length")
for i in range(n1):
    for j in range(n2):
        if list1[i] == list2[j]:
            both.append(list1[i])
print("same elements are")
print(both)
sum1=0
i=0
while i<=n1-1:
    sum1=sum1+list1[i]
    i=i+1
print("sum of list 1:",sum1)
sum2=0
j=0
while j<=n2-1:
    sum2=sum2+list2[j]
    j=j+1
print("sum of list 2:",sum2)
if sum1 == sum2:
    print("sum is same value")
else:
       print("sum is  not same value")
 

