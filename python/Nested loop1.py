# to print prime numbers in the given range

n1=int(input())
n2=int(input())
for i in range(n1,n2+1):
    c=0
    num=i
    while i>=1:
        if num%i==0:
            c+=1
        i-=1
    if c==2:
        print(num,end=' ')

'''

# to print prime numbers upto given number

n=int(input())
for i in range(1,n+1):
    c=0
    num=i
    while i>=1:
        if num%i==0:
            c+=1
        i-=1
    if c==2:
        print(num,end=' ')

'''
