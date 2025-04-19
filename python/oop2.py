class add:
    def add1(self,a,b):
        print(a+b)
    def Mod(self,a,b):
        print(a%b)
class sub(add):
    def sub1(self,a,b):
        print(a-b)
class Mul(add):
    def Mul1(self,a,b):
        print(a/b)
class Div(sub,Mul):
    def div(self,a,b):
        print(a/b)

print('First child')
ob=Mul()
ob.add1(20,3)
ob.Mul1(30,3)
print('Second Child')
ob1=sub()
ob1.add1(20,3)
ob1.sub1(40,5)
ob1.Mod(48,6)
print('Third class')
ob2=Div()
ob2.add1(2,3)
'''
class Account:
    def __init__(self,accName,accNo,accType,accBal):
        self.__accName=accName
        self.__accNo=accNo
        self.__accType=accType
        self.__accBal=accBal
        print('Account created successfully')
    def getAccName(self):
        return self.__accName
    def getAccNo(self):
        return self.__accNo
    def getAccType(self):
        return self.__accType
    def getAccBal(self):
        return self.__accBal
    def deposit(self):
        amount=int(input('Enter the amount to deposit : '))
        self.__accBal+=amount
        print(f'Amount Deposited Successfully')
    def withdraw(self):
        amount=int(input('Enter the amount to withdraw : '))
        if self.__accBal<amount:
            print('In-sufficient Balance')
            return
        self.__accBal-=amount
    def displayDetails(self):
        print('Account Details...')
        print(f'Account holder : {self.__accName}')
        print(f'Account Number : {self.__accNo}')
        print(f'Account Type : {self.__accType}')
        print(f'Account current balance : {self.__accBal}')
acc = Account('RAMANA RAJU',234561,'Savings',100000)
acc.deposit()
acc.displayDetails()


class Circle:
    def setRadius(s,r,pi=3.14):
        s.r=r
        s.pi=pi
    def area(s):
        s.a=s.pi*(s.r**2)
        print(s.a)
    def circum(s):
        s.p=2*s.pi*s.r
        print(s.p)
c=Circle()
c.setRadius(5)
c.area()
c.circum()
'''