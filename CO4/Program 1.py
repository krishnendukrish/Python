class Rectangle():
 def __init__(self,length,breadth):
  self.length=length
  self.breadth=breadth
 def area(self):
  return(self.length*self.breadth)
 def perimeter(self):
  return(2*(self.length+self.breadth))
r1=Rectangle(6,10)
r2=Rectangle(11,5)
a1=r1.area()
a2=r2.area()
p1=r1.perimeter()
p2=r2.perimeter()
print("the area of first rectangle=",a1)
print("the perimeter of first rectangle=",p1)
print("the area of second rectangle=",a2)
print("the perimeter of second rectangle=",p2)
if(a1>a2):
 print("First rectangle is bigger than second")
else:
 print("second rectangle is bigger than first")
