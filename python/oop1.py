
class Data:
    def Fill(s):
        li=list(map(int,input().split()))
        s.li=li
    def display(s):
        for i in s.li:
            print(i,end='')
    def Max(s):
        if len(s.li)==0:
            return 0
        return max(s.li)
    def Min(s):
        if len(s.li)==0:
            return 0
        return min(s.li)
ob=Data()
ob.Fill()
ob.display()
p=ob.Max()
r=ob.Min()
print(f'Max number in list : {p}')
print(f'Min number in list : {r}')

'''
class Result:
    def inpt(s,rollNo,name,m1,m2,m3):
        s.rollNo=rollNo
        s.name=name
        s.m1=m1
        s.m2=m2
        s.m3=m3
    def show(s):
        print('Results')
        print(f'Roll number : {s.rollNo}')
        print(f'Student Name : {s.name}')
        print(f'telugu marks : {s.m1}')
        print(f'hindi marks : {s.m2}')
        print(f'english marks : {s.m3}')
    def total(s):
        s.Totalmarks=s.m1+s.m2+s.m3
        return s.Totalmarks
    def avg(s):
        s.avg=s.Totalmarks/3
        return s.avg
ob=Result()
ob.inpt(3,'ramu',75,80,85)
tm=ob.total()
av=ob.avg()
print(f'Total marks : {tm}')
print(f'Average marks : {av}')

        
    
class Book:
    def get(s):
        s.bid,s.pgs,s.price=map(int,input().split())
    def show(s):
        print('Details of Book')
        print(f'Book Id :{s.bid}')
        print(f'No of Pages : {s.pgs}')
        print(f'Price of Book :{s.price}')
    def set(s,bid,pgs,price):
        s.bid=bid
        s.pgs=pgs
        s.price=price
    def getPrice(s):
        return s.price
ob=Book()
ob1=Book()
ob.get()
p1=ob.getPrice()
ob1.set(14,200,115)
p2=ob1.getPrice()
if p1>p2:
    ob.show()
else:
    ob1.show()
    
   

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


class Marks:
    def set(s,m1,m2,m3):
        s.m1=m1
        s.m2=m2
        s.m3=m3
    def Sum(s):
        s.sum1=s.m1+s.m2+s.m3
        return s.sum1
    def Avg(s):
        s.avg=(s.m1+s.m2+s.m3)/3
        return s.avg
ob=Marks()
ob.set(5,10,15)
r1=ob.Sum()
r2=ob.Avg()
print(r1,r2)
        


class Student:
    def setStudDetails(self,rollNum,studName,mark1,mark2,mark3):
        self.rollNum=rollNum
        self.studName=studName
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def calculateTotal(self):
        self.totalMarks=self.mark1+self.mark2+self.mark3
    def displayStudioDetails(self):
        print('Student Details...')
        print(f'Student Name : {self.studName}')
        print(f'Student Roll No : {self.rollNum}')
        print(f'Student Total Marks : {self.totalMarks}')

ob=Student()
ob.setStudDetails(7,'Dhoni',92,95,97)
ob.calculateTotal()
ob.displayStudioDetails()

ob.setStudDetails(18,'Virat',80,85,87)
ob.calculateTotal()
ob.displayStudioDetails()



class Customer:
    def setCustDetails(s,cId,cName,cAddress):
        s.cId=cId
        s.cName=cName
        s.cAddress=cAddress
    def display(s):
        print('Customer Details')
        print(f'Customer Id : {s.cId}')
        print(f'Customer Name : {s.cName}')
        print(f'Customer Address : {s.cAddress}')

d=Customer()
d.setCustDetails('20701A04H5','Omkaram Subbaraju','3/4-A,Rameswaram,Sancharala,Porumamilla,Andhra Pradesh-516193')
d.display()  



class  Rectangle:
    def lengthBreadth(s,l,b):
        s.l=l
        s.b=b
    def area(s):
        s.a=s.l*s.b
    def perimeter(s):
        s.p=2*(s.l+s.b)
    def display(s):
        print('Rectangle parameters')
        print(f'length : {s.l}')
        print(f'breadth : {s.b}')
        print(f'Area : {s.a}')
        print(f'Perimeter : {s.p}')
rect=Rectangle()
rect.lengthBreadth(10,5)
rect.area()
rect.perimeter()
rect.display()
        


class Account:
    def __init__(self):
        self.accountNo='xxxxx'
        self.accountType='savings'
        self.accountBalance=0
    def setAccountDetails(self):
        self.accountNo = accountNo
        self.accountType = accountType
        self.accountBalance = accountBalance
    def withdraw(self,withdrawAmount=0):
        self.accountBalance-=withdrawAmount
    def deposit(self,deposit):
        self.accountBalance+=deposit
    def dispAccountDetails(self):
        print('Account Details')
        print(f'Account Number : {self.accountNo}')
        print(f'Account type : {self.accountType}')
        print(f'Account Balance : {self.accountBalance}')

subbu=Account()
subbu.deposit(100000)
subbu.withdraw(50000)
subbu.dispAccountDetails()
'''



