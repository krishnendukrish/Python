class Rectangle:
 def __init__(self,length,width):
  self.__length=length
  self.__width=width
 def area(self):
  return self.length*self.width
 def __lt__(self,other):
  return self.area()>other.area()
 r1=int(input("Eneter the length of first rectangle:"))
 w1=int(input("Eneter the width of first rectangle:"))
 rectangle1=(r1,w1)
 r2=int(input("Eneter the length of second rectangle:"))
 w2=int(input("Eneter the width of second rectangle:"))
 rectangle2=(r2,w2)
 if rectangle1 < rectangle2:
  print("Area of fisrt rectangle is smaller than second")
 else:
  print("Area of second rectangle is smaler than first")
