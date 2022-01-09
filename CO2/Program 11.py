a=int(input("enter the sides of square:"))
sqarea=lambda a:a*a
print("area of square is: ",sqarea(a))
l=int(input("enter the length of rectangle:"))
b=int(input("enter the breadth of rectangle:"))
rctarea=lambda l,b:l*b
print("area of rectangle is:",rctarea(l,b))
b=int(input("enter the base of the triangle:"))
h=int(input("enter the height of the triangle:"))
trarea=lambda b,h:.5*b*h
print("area of triangle is :",trarea(b,h))
