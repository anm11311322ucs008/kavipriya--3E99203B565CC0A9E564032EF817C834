# python program to create  Bankaccount class 
# with both a deposit () and a withdraw () function 
class Bank_Account:
      def __init__(self):
          self.balance=0
          print("Hello!!! welcome to the Deposit& withdrawal Machine")

      def deposit(self):
        amount=float(input ("Entet amount to be Deposited: ")) 
        self.balance += amount
        print (" \n amount Deposited:" ,amount)

      def withdraw(self):
        amount =float(input("Enter amount to be withdraw:  "))
        if self.balance>=amount:
           self.balance-=amount 
           print ("\n You withdrew:", amount)  
        else:
         print("\n Insufficient balance ")

      def display(self):
        print("\n Net Available balance=", self.balance)

# Driver  code 

# creating an object of class
s=Bank_Account()

# calling functions with that class object 
s.deposit()
s.withdraw()
s.display()
  

  

        