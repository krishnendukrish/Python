class Bank:
 def __init__(self,ac_no,name,type,balance):
  self.ac_no=ac_no
  self.name=name
  self.type=type
  self.balance=balance
 def display(self):
     print(self.ac_no)
     print(self.name)
 def deposit(self,amount):
  self.balance=self.balance+amount
  print("The amount deposited successfully....")
  return self.balance
 def withdraw(self,amount):
  if amount>self.balance:
   print("insufficient balance")
   return self.balance
  else:
   self.balance=self.balance-amount
   print("The amount withdrawed successfully....")
   return self.balance
a=Bank(1254,"Kiran","savings",10000)
a.display()
damount=float(input("Enter the amount to be deposited:"))
print("Your account balance:",a.deposit(damount))
wamount=float(input("Enter the amount to be withdrwn:"))
print("Your account balance:",a.withdraw(wamount))
