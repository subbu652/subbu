from multimethod import multimethod
class StudentRecord:
    @multimethod
    def __init__(self):
        self.name=None
        self.rollnum=0
        self.grade=None
    @multimethod
    def __init__(self,name:str,rollnum:int,grade:str):
        self.name=name
        self.rollnum=rollnum
        self.grade=grade
    @multimethod
    def __init__(self,name:str,rollnum:int,grade='F'):
        self.name=name
        self.rollnum=rollnum
        self.grade=grade

    def display(self):
        print(f'Student name : {self.name}')
        print(f'Roll Number  : {self.rollnum}')
        print(f'Grade        : {self.grade}')


ob=StudentRecord('Ramana Raju',30)
ob.display()
'''
from multimethod import multimethod
class Person:
    @multimethod
    def __init__(self):
        self.name=None
        self.age=0
    @multimethod
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
    @multimethod
    def __init__(self,name:str,age=0):
        self.name=name
        self.age=age
    def display(self):
        print(f'Person name : {self.name}')
        print(f'Age of person : {self.age} years\n')
ob=Person()
ob.display()
ob1=Person('Theja',24)
ob1.display()



from multimethod import multimethod
class Product:
    @multimethod
    def __init__(self):
        self.pname=""
        self.price=0
        self.quantity=0
    @multimethod
    def __init__(self,pname:str,price:int,quantity:int):
        self.pname=pname
        self.price=price
        self.quantity=quantity
    @multimethod
    def __init__(self,pname:str,price:int,quantity=0):
        self.pname=pname
        self.price=price
        self.quantity=quantity
    def display(self):
        print(f'Product name : {self.pname}')
        print(f'Product price : {self.price}')
        print(f'Product quantity : {self.quantity} kg')
a=Product()
a.display()

b=Product('Bike',100000)
b.display()


from multipledispatch import dispatch
class Book:
    @dispatch()
    def __init__(self):
        self.title=None
        self.author=None
        self.year=0
    @dispatch(str,str,int)
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    @dispatch(str,str)
    def __init__(self,title,author,year=0):
        self.title=title
        self.author=author
        self.year=year

    def Display(self):
        print(f'Title of Book : {self.title}')
        print(f'Author of Book : {self.author}')
        print(f'Publication Year : {self.year}')
ob=Book()
ob.Display()

ob=Book("The Lion King",'Subbu',2010)
ob.Display()



from multimethod import multimethod
class BankAccount:
    @multimethod
    def __init__(self):
        self.accountNumber=None
        self.initialBalance=0
    @multimethod
    def __init__(self,accountNumber:int,initialBalance:int):
        self.accountNumber=accountNumber
        self.initialBalance=initialBalance
    @multimethod
    def __init__(self,accountNumber:int,initialBalance=0):
        self.accountNumber=accountNumber
        self.initialBalance=initialBalance

    def display(self):
        print(f'Account Number :{self.accountNumber}')
        print(f'Initial Balance : {self.initialBalance}\n')
ob=BankAccount()
ob.display()

ob1=BankAccount(2160700456,20000)
ob1.display()



from multipledispatch import dispatch
class Car:
    @dispatch()
    def __init__(self):
        self.make=None
        self.model=None
        self.year=0
    @dispatch(str,str,int)
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    @dispatch(str, str,)
    def __init__(self, make, model, year=0):
        self.make = make
        self.model = model
        self.year = year
    def displayDetails(self):
        print(f'make : {self.make}')
        print(f'model : {self.model}')
        print(f'year : {self.year}\n')
ob=Car()
ob.displayDetails()

ob1=Car('Tata','Nano',2015)
ob1.displayDetails()



from multipledispatch import dispatch
class Student:
    @dispatch()
    def __init__(self):
        self.name = 'xxxxx'
        self.rollNumber = 0
    @dispatch(str,int)
    def __init__(self,name,rollNumber):
        self.name=name
        self.rollNumber=rollNumber

    @dispatch(str,int)
    def __init__(self, name,rollNumber=0):
        self.name = name
        self.rollNumber = rollNumber

    def displayDetails(self):
        print(f'Name : {self.name}')
        print(f'Roll Number : {self.rollNumber}')

ob = Student('subbu', 70)
ob.displayDetails()



from multimethod import multimethod
class Employee:
    @multimethod
    def __init__(self):
        self.name='xxxxx'
        self.Id=0
    @multimethod
    def __init__(self,name:str,Id:int):
        self.name=name
        self.Id=Id
    @multimethod
    def __init__(self,name:str):
        self.name=name
        self.Id=0
    def displayDetails(self):
        print(f'Name : {self.name}')
        print(f'Id : {self.Id}')
ob=Employee('subbu',70)
ob.displayDetails()



from multimethod import multimethod
@multimethod
def add(a:str,b:int):
    print(a*b)
@multimethod
def add(a:int,b:str):
    print(a*b)
add(6,'s')



from multimethod import multimethod
class Rectangle:
    @multimethod
    def __init__(self):
        self.length=0
        self.width=0
    @multimethod
    def __init__(self,length:int,width:int):
        self.length=length
        self.width=width
    @multimethod
    def __init__(self,sidelength:int):
        self.length=sidelength
        self.width=sidelength

    def displayDetails(self):
        print(f'length : {self.length}')
        print(f'width : {self.width}')
ob=Rectangle(5)
ob.displayDetails()



from multimethod import multimethod
@multimethod
def add(a:int,b:int):
    print(a+b)
@multimethod
def add(a:int,b:int,c:int):
    print(a+b+c)
add(2,3)
add(2,3,5)
'''