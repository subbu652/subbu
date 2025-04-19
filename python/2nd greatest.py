n = int(input("Enter a number: "))
a,b = 0,1
for i in range(n):
    print(a,end=" ")
    a,b = b,a+b

'''
s = str(input())
n=len(s)
while n!=0:
    print(s[len(s)-n])
    n=n-1


n = int(input())
p = []
num = 2
while len(p) < n*(n+1)//2:
    if all(num%i != 0 for i in range(2,int(num**0.5)+1)):
        p.append(num)
    num += 1
for i in range(1,n+1):
    s,m=i-1,n-1
    for j in range(1,i+1):
        print(p[s],end=' ')
        s+=m
        m-=1
    print()

def create():
    f = open('atm.txt','a')
    BankName = input('Enter Bank Name : ')
    AccNumber = input('Enter Account Number : ')
    AH_name = input('Account Holder Name : ')
    IFSCode = input('Enter IFScode : ')
    CardNumber = input('Enter your Card number : ')
    f.write(f'BankName : {BankName},AccountNumber : {AccNumber},AHN : {AH_name},IFSCode : {IFSCode},CardNumber : {CardNumber}')
    print('You have applied for ATM successfully')
    f.close()
'''